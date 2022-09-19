import json
import cv2
import numpy as np
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import rgbToGray as rTg


def imgCluster(id):
    # 이미지 읽기
    src = 'src/images/'
    url = src + id + '/0.jpg'
    data = []
    print('url : ', url)
    img = cv2.imread(url, cv2.IMREAD_COLOR)
    # BGR -> RGB 이미지 변환
    # print(img)
    # 1. 이미지 없을때,
    try:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # shape 변환??
        img = img.reshape((img.shape[0] * img.shape[1], 3))
    except BaseException as error:
        print('An exceptionoccurred: {}'.format(error))
        data.append({'error': True, 'message': "에러발생"})
    # except ValueError:
    #     print(ValueError)
    #     return json.dumps({'error': '밸류에러'})
    # except AttributeError:
    #     print(AttributeError)
    #     return json.dumps({'error': '속성에러'})
    # except cv2.error:
    #     print(cv2.error);
    #     return json.dumps({'error': 'cv2에러'})
    print(data, bool(data))
    if not bool(data):

        k = 3
        clt = KMeans(n_clusters=k)
        clt.fit(img)

        hist = centroid_histogram(clt)

        print('hist : ', hist)

        for i in range(0, len(clt.cluster_centers_)):
            if hist.any():
                print(i, clt.cluster_centers_[i], hist[i])
                g = rTg.rgbToGray(clt.cluster_centers_[i])
                print('g : ', g)
                data.append(
                    {
                        'color': list(clt.cluster_centers_[i]),
                        "hist": hist[i],
                        "gray": g
                    })
            else:
                data.append({
                    'color': list(['#ffffff', '#ffff00', '#000000']),
                    "hist": list([0.2, 0.3, 0.5]),
                    "gray": 0
                })

    return json.dumps(data)


def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist


# hist = centroid_histogram(clt)
# print(hist)
