from os import path, listdir
import sys
from sklearn import svm
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib

DATA_DIR = 'dataset'
classes = ['anger', 'fear', 'sadness', 'surprise', 'happiness', 'neutral', 'disgust']

def load_dataset():
	# Read the data
	train_data = []
	train_labels = []
	test_data = []
	test_labels = []
	iterator = 0

	for curr_class in classes:
		dirname = path.join(DATA_DIR, curr_class)
		for fname in listdir(dirname):
			if iterator > 5000:
				iterator=0 
				break
			iterator = iterator + 1
			with open(path.join(dirname, fname), 'r') as f:
				content = f.read()
				if iterator > 4000:
					test_data.append(content)
					test_labels.append(curr_class)
				else:
					train_data.append(content)
					train_labels.append(curr_class)
	return train_data, train_labels, test_data, test_labels

def main():
	train_data, train_labels, test_data, test_labels = load_dataset()
	vectorizer = TfidfVectorizer(min_df=5,
                                 max_df = 0.85,
                                 sublinear_tf=True,
                                 use_idf=True)

	vectorizer.fit(train_data+test_data)

	joblib.dump(vectorizer, 'vectorizer.pkl')

	vectorized_train_data = vectorizer.transform(train_data)
	vectorized_test_data = vectorizer.transform(test_data)

	classifier = svm.SVC(kernel='linear', C=10, probability=True, verbose=1)
	classifier.fit(vectorized_train_data, train_labels)

	joblib.dump(classifier, 'model.pkl')
		
	# while True:
	# 	var = input("Please enter something: ")
	# 	our_test = vectorizer.transform([var])
	# 	prediction_rbf = classifier.predict(our_test)
	# 	priediction_proba = classifier.predict_proba(our_test)
	# 	print(zip(classifier.classes_, priediction_proba[0])) #shows all propabilities
	# 	print(prediction_rbf) #shows determined label


if __name__ == "__main__":
	main()