# 费孝通·文化自觉与实地洞察

访谈取证、关系情境、跨文化理解：有资料依据、有使用边界、可复核的中文 Agent Skill。

## 安装与使用
公开仓库直接提供 Skill，不依赖 GitHub Release。
```sh
npx skills add constantin2088/fei-xiaotong-fieldwork-skill
```
也可将仓库内容复制到支持该格式的客户端 Skill 目录，保留以 `fei-xiaotong-fieldwork-skill` 命名的文件夹和根目录 SKILL.md。客户端支持范围以其文档为准。安装后提出具体任务，由客户端按描述加载。

**试用任务**：三名海外访谈者不愿绑卡，团队归因为当地人不信任中国公司。

## 内容
- [执行说明](SKILL.md)
- [资料卡](references/sources.md)、[工作表](references/frameworks.md)、[边界](references/boundaries.md)
- [三个示例](examples/demo.md)、[八个行为评测场景](evals/test-cases.md)

## 验证与贡献
```sh
python scripts/check_skill.py . --release
python -m unittest discover -s tests -v
python scripts/check_links.py
```
`--release` 是完整性检查参数，不创建 GitHub Release。CI 在每次提交运行上述检查。独立客户端模型行为评测尚未执行；用例、结构检查与实际模型能力分开报告。
修改时提供来源和定位，区分原文与转译；运行检查后直接提交到仓库。不要创建发布附件作为必需安装步骤。系列标识、链接和推荐由总仓库 catalog/skills.json 同步，避免手工修改受管理区块。

## 许可
项目原创内容使用 [MIT](LICENSE)。链接所指第三方作品保留原权利，本仓库不重新许可它们。

## 与人物模仿的区别
本项目提供可复核的工作流，不冒充本人，不把历史思想当现代事实保证。每个示例给出判断依据、反例或失败条件，适合实际任务后继续修订。
