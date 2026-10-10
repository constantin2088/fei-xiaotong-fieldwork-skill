"""Count declared evidence types; never estimate population prevalence."""
def summarize(records):
 counts={'observation':0,'participant_report':0,'researcher_inference':0}
 ids=set()
 for r in records:
  if not isinstance(r,dict):raise ValueError('record must be an object')
  ident=r.get('id');kind=r.get('kind')
  if not isinstance(ident,str) or not ident.strip() or ident in ids:raise ValueError('unique id required')
  ids.add(ident)
  if kind not in counts:raise ValueError('separate evidence type required')
  if not isinstance(r.get('context'),str) or not r['context'].strip():raise ValueError('context required')
  if not isinstance(r.get('locator'),str) or not r['locator'].strip():raise ValueError('record locator required')
  counts[kind]+=1
 return counts
