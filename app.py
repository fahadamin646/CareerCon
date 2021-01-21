from flask import Flask, request
app = Flask(__name__)
import pandas as pd
import pickle
import Process as pr
@app.route('/')
def myfunct():
    return 'Hello'
@app.route('/getPredict',methods=['POST','GET'])
def hello_world():
    PubSpeak=request.form['PubSpeak']
    WorkLong=request.form['WorkLong']
    SelfLearn=request.form['SelfLearn']
    ExtraCourse=request.form['ExtraCourse']
    TalentTest=request.form['TalentTest']
    Olympiad=request.form['Olympiad']
    ReadingWriting=request.form['ReadingWriting']
    CapScore=request.form['CapScore']
    Job=request.form['Job']
    TakenInput=request.form['Takeninput']
    Games=request.form['Games']
    Realationship=request.form['Relationship']
    Behaviour=request.form['Behaviour']
    Management=request.form['Management']
    HardWorker=request.form['HardWorker']
    WorkedInTeam=request.form['WorkedInTeam']
    Introvert=request.form['Introvert']
    pred = pr.getPrediction(PubSpeak,WorkLong,SelfLearn,ExtraCourse,TalentTest,Olympiad,ReadingWriting,CapScore,Job,TakenInput,Games,Relationship,Behaviour,Management,HardWorker,WorkedInTeam,Introvert)
    return str(pred)