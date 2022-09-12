
import pickle

def gauti_zurnala():
    try:
        with open("zurnalas.pkl", 'rb') as file:
            zurnalas = pickle.load(file)
            return zurnalas
    except:
        with open("zurnalas.pkl", 'wb') as file:
            zurnalas = []
            pickle.dump(zurnalas, file)
            return zurnalas

def irasyti_zurnala():
    with open("zurnalas.pkl", 'wb') as file:
        pickle.dump(zurnalas, file)


zurnalas = gauti_zurnala()
