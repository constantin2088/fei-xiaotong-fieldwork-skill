<!-- SERIES:START -->
> **属于 [Chinese Thinkers as Skills 系列](https://github.com/constantin2088/chinese-thinkers-skills)** · [完整作品目录](https://github.com/constantin2088/chinese-thinkers-skills#作品目录)

**相关推荐**：[梁启超·自新与变局](https://github.com/constantin2088/liang-qichao-skill) · [叶茂中·冲突营销](https://github.com/constantin2088/ye-maozhong-skill) · [陈寅恪·深度研究](https://github.com/constantin2088/chen-yinke-research-skill) · [蔡元培·多元协作](https://github.com/constantin2088/cai-yuanpei-skill) · [宋志平·经营管理](https://github.com/constantin2088/song-zhiping-management-skill) · [许倬云·系统思维](https://github.com/constantin2088/xu-zhuoyun-systems-skill) · [陶行知·教学做合一](https://github.com/constantin2088/tao-xingzhi-learning-skill) · [严复·概念转译与论证校核](https://github.com/constantin2088/yan-fu-translation-skill) · [黄宗羲·制度问责与公共评议](https://github.com/constantin2088/huang-zongxi-governance-skill) · [顾炎武·经世问题研究](https://github.com/constantin2088/gu-yanwu-practical-skill) · [张载·共同体责任](https://github.com/constantin2088/zhang-zai-responsibility-skill) · [戴震·概念与人情辨析](https://github.com/constantin2088/dai-zhen-concepts-skill) · [王充·问难与实证](https://github.com/constantin2088/wang-chong-skepticism-skill) · [章学诚·文献义例与史德](https://github.com/constantin2088/zhang-xuecheng-documentation-skill) · [傅斯年·材料与工具规划](https://github.com/constantin2088/fu-sinian-evidence-skill) · [钱穆·历史文化脉络](https://github.com/constantin2088/qian-mu-context-skill) · [梁漱溟·社区协作实验](https://github.com/constantin2088/liang-shuming-community-skill) · [晏阳初·生活能力建设](https://github.com/constantin2088/yan-yangchu-education-skill) · [叶圣陶·诚实写作与自改](https://github.com/constantin2088/ye-shengtao-writing-skill) · [朱光潜·审美观察与判断](https://github.com/constantin2088/zhu-guangqian-aesthetics-skill) · [宗白华·意境与空间节奏](https://github.com/constantin2088/zong-baihua-artistic-skill) · [刘勰·文思与篇章构造](https://github.com/constantin2088/liu-xie-composition-skill) · [刘知几·叙事偏差审查](https://github.com/constantin2088/liu-zhiji-narrative-skill) · [沈括·观察与试验辨误](https://github.com/constantin2088/shen-kuo-observation-skill) · [宋应星·工艺与生产系统](https://github.com/constantin2088/song-yingxing-process-skill) · [徐光启·知识引入与试验](https://github.com/constantin2088/xu-guangqi-adaptation-skill) · [冯友兰·行动意义反思](https://github.com/constantin2088/feng-youlan-reflection-skill) · [郑观应·产业能力与竞争](https://github.com/constantin2088/zheng-guanying-commerce-skill) · [颜元·实习与能力验收](https://github.com/constantin2088/yan-yuan-practice-skill)

> 系列入口与推荐由总仓库 catalog/skills.json 生成。
<!-- SERIES:END -->

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
