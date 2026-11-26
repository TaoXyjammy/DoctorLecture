# 运动训练负荷的因果分析

谢淘的高校教师岗位科研汇报。使用 LaTeX Beamer 和 [Metropolis](https://github.com/matze/mtheme) 主题。演示 PDF 有 11 页主讲、3 页备查。逐页讲稿及时间安排在源码的 `\talk` 中。

- [演示 PDF](research-talk.pdf)
- [可编辑 XeLaTeX 源码](research.tex)

在此目录使用 TeX Live（含 Beamer、Metropolis、fontspec、PGF/TikZ 和 booktabs），并安装 Noto Sans CJK SC 字体。

```sh
xelatex -interaction=nonstopmode -halt-on-error -jobname=research-talk research.tex
xelatex -interaction=nonstopmode -halt-on-error -jobname=research-talk research.tex
```

如需编译出带讲稿的版本，在源码中启用 `\setbeameroption{show notes}`。正文的体育因果推断背景依据 Simon Nolte 2024 年硕士论文 *More Than Just Associations* 的 Introduction。图表文件为谢淘两篇论文的标注出处节选，未收录论文全文。
