# 中文编译与文献计量复现

当前工程采用所提供 MUL-Talk 模板的 mul-beamer.cls 和原版封面背景、模板标识。作者教育经历见封面署名。进入本目录，用 XeLaTeX 编译 main.tex 两次。环境需有 Noto Sans CJK SC、Beamer、fontspec、TikZ、marvosym 和 booktabs。PowerPoint 为 PDF 的逐页放映版，编辑入口为 main.tex。

## 当前版本的 Google Scholar 统计口径

以 2021–2025 五个完整年为范围，使用英文检索式 `"sports injury" correlation` 和 `"sports injury" "causal inference"`。记录两组页面显示的五年估计命中数，第二组另按五个单年检索。Google Scholar 返回 403，当前正文用有出处的跑鞋队列解释研究背景。上述英文检索只覆盖特定表述，不代表全学科普查。

## 早期版本的 Web of Science 备选检索方案

Web of Science Core Collection，Sport Sciences 类别，Article，五个完整出版年 2021–2025。记录实际检索日期、订阅覆盖的引文索引、数据库更新日期。当前未取得数据库返回，未报告计数。下列检索按方法关键词识别文献，关键词命中数只近似反映方法使用情况。

在高级检索中按顺序执行以下四个集合。

```
#1 WC=("Sport Sciences") AND PY=(2021-2025) AND DT=(Article)
#2 #1 AND TS=("correlation analys*" OR "correlational stud*" OR "correlation coefficient*" OR "Pearson* correlation*" OR "Spearman* correlation*")
#3 #1 AND TS=("causal inferen*" OR "causal discover*" OR "causal effect*" OR "target trial emulat*" OR "marginal structural model*" OR "g-formula" OR "g-computation" OR "instrumental variable*" OR "Mendelian randomization" OR "Mendelian randomisation")
#4 #2 AND #3
```

每次输入等号以后的检索内容或对应集合组合，由 WoS 分配集合号。先创建 #1，再用 #1 与相应 TS 条件组合。按 Publication Years 分析 #2、#3、#4。#2 为相关研究关键词命中数，#3 为因果研究关键词命中数，#4 为同时命中两组关键词的记录。三者不可直接相加。以 WoS 集合总记录数核对逐年求和，检查 Early Access 与最终出版年等口径差异。抽查命中文献，记录误命中与漏检风险。

将经核对的计数填入 UTF-8 CSV，表头为 year,association,causal,both，五行依次对应 2021 至 2025。只在数据库确认该年无记录时填 0。执行 `python plot_wos.py input.csv` 可生成 WoS 统计图。
