# TensorFlow + Keras 实现基于图像语义分割的“魔法换天”功能

使用 TensorFlow + Keras 实现的基于图像语义分割的“魔法换天”功能。

然而我太菜了，最终效果并不是很好（摊手）。<s>啊？就这？你也好意思挂上来？</s>

我也不知道我最后整出了个什么东西，反正应付期末大作业就对了；部分效果较好的最终成果图如下所示（左一为原图，其它均为换天处理后的图片）：

![image.png](https://i.loli.net/2020/06/29/6KoxaY2ChSdgGV7.png)

![image.png](https://i.loli.net/2020/06/29/YksP5p7XwqQ2l3t.png)

## 说明

不想打字废话了，详见[课程报告](report.pdf).

语义分割采用的是 RefineNet 神经网络实现：[论文地址](https://arxiv.org/abs/1611.06612).

数据集部分由自己拍摄、收集、处理；另一部分来自 [skyfinder 数据集](https://mypages.valdosta.edu/rpmihail/skyfinder/)。处理数据的 Python 工具程序和数据集的格式样例详见上传的代码中 `utils` 目录和 `dataset-example` 目录。

数据集和预训练好的模型太大了（前者 1.1G，后者 300+M），小水管传不上来，懒得传了；有需要的话可以联系我或者提个 issue 什么的，不过大概是没人会对这种效果的东西感兴趣的。

## Licence

`semantic-segmentation-based-sky-replacement` 是 Yume Maruyama 完成的厦门大学信息学院计算机系 2020 春季学期《模式识别》课程的期末设计；在 MIT 协议下开源。

你可以在课程报告的附录中，了解项目所引用和参考的材料。
