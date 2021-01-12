# -*- coding: utf-8 -*-
import functools, json, requests

from flask import flash, redirect, render_template, request
from flask import Blueprint, session, url_for, g

from app.services.vid_to_spec_converter import Converter
import os
import glob
from os import path
from fastai.basics import load_learner


blueprint = Blueprint('music_classifier', __name__, url_prefix='/music_classifier')
convert = Converter()
learn_inf = load_learner('app/static/fastai_model/export.pkl')

@blueprint.route('/')
def base():
    if(not path.exists('app/static/spectrogram')):
        os.mkdir('app/static/spectrogram')

    for f in glob.glob("app/static/spectrogram/*.png"):
        os.remove(f)

    g.classified = False
    return render_template('music_classifier/classify.html')


@blueprint.route('/classify')
def classify():
    for f in glob.glob("app/static/spectrogram/*.png"):
        os.remove(f)
    g.classified = True
    search = request.args.get('query', '')
    name = convert.convert_yt_to_mel_spec(yt_link=search)
    pred, pred_idx, probs= learn_inf.predict(f'app/static/spectrogram/{name}.png')
    g.path_to_image = f'/static/spectrogram/{name}.png'
    print(pred)
    print(probs)
    print(g.path_to_image)
    g.classification = pred
    g.confidence = f"{probs[pred_idx]*100:.04}%"
    return render_template('music_classifier/classify.html', query=search)


@blueprint.after_request
def add_header(response):
    response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response
