import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from fieldnotes import summarize
class DomainTests(unittest.TestCase):
 def test_distinguish_evidence(self):self.assertEqual(summarize([{'id':'a','kind':'participant_report','context':'付款退出','locator':'脱敏访谈01'}])['observation'],0)
 def test_inference_not_report(self):self.assertEqual(summarize([{'id':'a','kind':'researcher_inference','context':'工作假设','locator':'分析笔记01'}])['researcher_inference'],1)
 def test_unknown_kind(self):
  with self.assertRaises(ValueError):summarize([{'id':'a','kind':'fact','context':'x','locator':'y'}])
 def test_missing_context(self):
  with self.assertRaises(ValueError):summarize([{'id':'a','kind':'observation','locator':'y'}])
 def test_duplicate(self):
  with self.assertRaises(ValueError):summarize([{'id':'a','kind':'observation','context':'x','locator':'y'}]*2)
