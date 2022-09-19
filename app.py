from flask import Flask, jsonify, request
import json
import imgCluster
app = Flask(__name__)


@app.route('/image')
def hello_world():
    # 쿼리에서 url 값 확인
    query_dict = request.args.to_dict()
    id = query_dict['id']
    # 클러스터 모듈에 url 값 전달
    # print(id, instaId)
    if(id):
        data = imgCluster.imgCluster(id)
    else:
        return print('오류오류')
    # print('typeof ', type(data), data)
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
