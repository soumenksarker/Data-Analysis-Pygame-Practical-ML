import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
print(digits.data)
print(digits.target)
clf = svm.SVC(gamma = 0.001, C = 100)

print(len(digits.data))

x,y = digits.data[:-1], digits.target[:-1]
clf.fit(x,y)

print('Prediction', clf.predict(digits.data[-5]))
plt.imshow(digits.images[-5], cmap = plt.cm.gray_r, interpolation = 'nearest')
plt.show()
