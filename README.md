<!-- SERIES:START -->
> **属于 [Chinese Thinkers as Skills 系列](https://github.com/constantin2088/chinese-thinkers-skills)** · [完整作品目录](https://github.com/constantin2088/chinese-thinkers-skills#作品目录)

**相关推荐**：[梁启超·自新与变局](https://github.com/constantin2088/liang-qichao-skill) · [叶茂中·冲突营销](https://github.com/constantin2088/ye-maozhong-skill) · [陈寅恪·深度研究](https://github.com/constantin2088/chen-yinke-research-skill) · [蔡元培·多元协作](https://github.com/constantin2088/cai-yuanpei-skill) · [宋志平·经营管理](https://github.com/constantin2088/song-zhiping-management-skill) · [许倬云·系统思维](https://github.com/constantin2088/xu-zhuoyun-systems-skill)

> 系列入口与推荐由总仓库 catalog/skills.json 生成。
<!-- SERIES:END -->

# Thinkers Skill Template / 中国思想家 Agent Skill 开发模板

**A small, dependency-free starter for research-grounded Agent Skills.**

本仓库是 Chinese Thinkers as Skills 系列的开发模板，**不是一个可以直接安装的成品 Skill**。它提供生成器、史料卡、评测模板与发布检查，帮助每个新项目保持统一工程质量、保留独特的方法论。

[系列首页](https://github.com/constantin2088/chinese-thinkers-skills) · [官方 Agent Skills 规范](https://agentskills.io/specification) · [贡献规范](CONTRIBUTING.md)

## 60 秒创建一个新 Skill

```bash
python scripts/new_skill.py \
  --slug chen-yinke-research-skill \
  --name-zh "陈寅恪" \
  --focus "史料互证与深度研究" \
  --output ./dist
```

会生成 `dist/chen-yinke-research-skill/`，其中包含 `SKILL.md`、README、史料表、现代转译边界、Demo 和评测文件。

```bash
python scripts/check_skill.py dist/chen-yinke-research-skill
```

生成结果**只是一个需要研究和填写的草案**。除非补齐标记内容并通过发布检查，否则不要公开宣传为完成的历史人物 Skill。

```bash
python scripts/check_skill.py dist/chen-yinke-research-skill --release
```

`--release` 会拒绝任何 `TODO:` 标记，并检查核心文件存在、Skill 名称和 frontmatter 合规。

## 开发步骤

1. 找到足够的一手作品和可核查资料，填好 `references/sources.md`。
2. 为人物建立真正独特的方法论，不要从别人的 Skill 直接替换姓名。
3. 把来源观点与项目现代转译分层，标出失效边界。
4. 写出能在真实任务上逐步执行的工作流。
5. 加入真实案例、负面案例、误触发与边界测试。
6. 运行结构检查，在目标 Agent 里做实际安装与回答测试。
7. 审核历史引语、版权与隐私后再发布。

## 技术原则

- 只需要 Python 3.9+ 标准库，不依赖外部服务。
- `SKILL.md` 是 Agent Skills 核心入口，需要 YAML `name` / `description`。
- 多文档采用渐进披露：核心流程在 `SKILL.md`，证据和详细研究在 `references/`。
- 不是历史人物 Persona、宣传工具，也不授予任何现代事件的虚构背书。

## 测试

```bash
python -m unittest discover -s tests -v
```

## License

MIT License · Maintainer: [constantin2088](https://github.com/constantin2088)
## 系列关联自动继承

新人物会自动带上系列标识、总仓库回链、已发布作品推荐与每日 README 刷新工作流。模板快照由总仓库发布脚本生成；请勿手改作品列表。

发布后运行 `python scripts/sync_series.py --slug <仓库名>` 刷新 README，运行 `python scripts/sync_series.py --slug <仓库名> --metadata --apply` 同步 GitHub About。统一 Topics、Website 与推荐来自 [唯一目录](https://github.com/constantin2088/chinese-thinkers-skills/blob/main/catalog/skills.json)。About 操作需要已有管理登录；普通 CI 只写本仓库 README。
