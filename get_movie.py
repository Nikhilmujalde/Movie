import json
import numpy as np
import pandas as pd
import pickle
from flask import Flask, jsonify, request
# from flask_cors import CORS
from flask_cors import CORS


def get_movie():
    # print(movies['title'].values)
    # return movies['title'].tolist()
    movies = ["Avatar","second"]
    return movies

def recommend(movie_name):
    
    recommended_movie = ["Avatar"]
    
    return recommended_movie

my_movies =  get_movie()
# print(my_movies)

recomendation = recommend('Avatar')
# print(recomendation)

    

if __name__ == '__main__':
    print("We are in get movies name")
    