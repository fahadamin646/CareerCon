import pandas as pd
import pickle
def getPrediction(PubSpeak,WorkLong,SelfLearn,ExtraCourse,TalentTest,Olympiad,ReadingWriting,CapScore,Job,TakenInput,Games,Relationship,Behaviour,Management,HardWorker,WorkedInTeam,Introvert):
    lst=[[PubSpeak,WorkLong,SelfLearn,ExtraCourse,TalentTest,Olympiad,ReadingWriting,CapScore,Job,TakenInput,Games,Relationship,Behaviour,Management,HardWorker,WorkedInTeam,Introvert]]
    df=pd.DataFrame(lst,columns=['public speaking points','can work long time before system?','self-learning capability?','Extra-courses did','talenttests taken?','olympiads','reading and writing skills','memory capability score','Job/Higher Studies?','Taken inputs from seniors or elders','interested in games','In a Realtionship?','Gentle or Tuff behaviour?','Management or Technical','hard/smart worker','worked in teams ever?','Introvert'])
    with open('stand_scalar', 'rb') as f:
        sc=pickle.load(f)
    with open('model', 'rb') as f:
        ppn = pickle.load(f)
    dataf=sc.transform(df)
    pred=ppn.predict(dataf)
    return str(pred[0])

