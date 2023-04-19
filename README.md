# HandwritingAI
설명: 나의 손글씨를 인공지능에게 학습시킨 후 손글씨 인식 인공지능 모델 생성

인공지능 모델 생성 코드 오류 해결과정
1. TensorFlow 모듈 설치 pip install tensorflow
2. Matplotlib 모듈 설치 pip install matplotlib
-Matplotlib 모듈: 데이터 시각화를 위한 파이썬 라이브러리로, 일반적으로 데이터 분석이나 머신 러닝에서 많이 사용
3. 손글씨 이미지 파일 확장자 옳바르게 입력(jpg->png로 수정)
4. print('내가 본 글자는 ', model.predict_classes(x_test[n].reshape((1, 28, 28)))) 오류
predict_classes() 함수는 예전 버전의 함수로 더 이상 사용되지 않음.
대신 predict()로 수정하여 사용.
