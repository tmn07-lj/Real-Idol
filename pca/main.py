#coding=utf-8
# http://ufldl.stanford.edu/wiki/index.php/%E4%B8%BB%E6%88%90%E5%88%86%E5%88%86%E6%9E%90
# http://blog.csdn.net/u012162613/article/details/42177327
# http://www.cnblogs.com/hdu-2010/p/4381533.html
import numpy as np
from PIL import Image
#零均值化  
def zeroMean(dataMat):        
    meanVal=np.mean(dataMat,axis=0)     #按列求均值，即求各个特征的均值  
    newData=dataMat-meanVal  
    return newData,meanVal  
  
def pca(dataMat,n):  
    newData,meanVal=zeroMean(dataMat)  
    covMat=np.cov(newData,rowvar=0)    #求协方差矩阵,return ndarray；若rowvar非0，一列代表一个样本，为0，一行代表一个样本  
      
    eigVals,eigVects=np.linalg.eig(np.mat(covMat))#求特征值和特征向量,特征向量是按列放的，即一列代表一个特征向量  
    # print (eigVals)
    eigValIndice=np.argsort(eigVals)            #对特征值从小到大排序  
    n_eigValIndice=eigValIndice[-1:-(n+1):-1]   #最大的n个特征值的下标  
    n_eigVect=eigVects[:,n_eigValIndice]        #最大的n个特征值对应的特征向量  
    lowDDataMat=newData*n_eigVect               #低维特征空间的数据  
    reconMat=(lowDDataMat*n_eigVect.T)+meanVal  #重构数据  
    return lowDDataMat,reconMat  

def preprocess():
    im = Image.open('haha.jpg')
    r,b,g = [],[],[]
    for i in xrange(im.size[0]):
        tr,tb,tg = [],[],[]
        for j in xrange(im.size[1]):
            tr.append(im.getpixel((i,j))[0])
            tb.append(im.getpixel((i,j))[1])
            tg.append(im.getpixel((i,j))[2])
        r.append(tr)
        b.append(tb)
        g.append(tg)
    return r,b,g
def rebuild(r,b,g):
    im = Image.open('haha.jpg')
    for i in xrange(im.size[0]):
        for j in xrange(im.size[1]):
            im.putpixel((i,j),(r[i,j],b[i,j],g[i,j]))
    im.save('pca.jpg')
    return r,b,g

def main():
    r,b,g = preprocess()

    r = np.array(r)
    b = np.array(b)
    g = np.array(g)
    print (r.shape)

    k = 3
    rr = pca(r,k)
    rb = pca(b,k)
    rg = pca(g,k)

    # print (rr[0])
    print rr[0].shape

    # x = rr[1]
    # print x[1,1]
    # print (rr[1][0][0][0])
    # rebuild(rr[1],rb[1],rg[1])


if __name__ == '__main__':
    main()
    # print (re[1])

# im = Image.open('haha.jpg')

# im = im.convert('1')
# im.save('result.png')
# print im.getpixel((1,1))
# I = np.asarray(im)
# re =np.dsplit(I,3)
# print(re[0])
# r = pca(re[0],100)
# b = pca(re[1],100)
# g = pca(re[2],100)

# # pca(I,10)



# # print (I)
# im = Image.fromarray(np.uint8(I))

# print (im)

# re = pca(I,10)

# print (re[0])
# print (re[1])