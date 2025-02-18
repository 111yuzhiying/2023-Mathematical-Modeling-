from LSTM import stockLSTM
from torchviz import make_dot
from preprocess import preprocess
import torch
import torch.nn.functional as F
def viz():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    x=torch.from_numpy(preprocess('000006.xlsx'))
    x=x.to(torch.float32)
    x = x.unsqueeze(0)
    if torch.cuda.is_available():
        x = x.cuda()
    model = stockLSTM(16,64,1,6)  # 获取网络的预测值
    model.to(device)
    model.eval()
    y = model(x)
    print(y)
    MyConvNetVis = make_dot(y, params=dict(list(model.named_parameters()) + [('x', x)]))
    MyConvNetVis.format = "png"
    # 指定文件生成的文件夹
    MyConvNetVis.directory = "data"
    MyConvNetVis.view()
import hiddenlayer as h

if __name__ == '__main__':
    viz()