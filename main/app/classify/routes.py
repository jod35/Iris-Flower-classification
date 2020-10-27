from flask import Blueprint,render_template,request,redirect,url_for,flash
import numpy as np
from .predict import predict_flower_class,iris_dataset




app_blueprint=Blueprint('app',__name__,template_folder='templates',static_folder='static')


@app_blueprint.route('/',methods=['GET', 'POST'])
def index():
    target_name=""
    context={}
    if request.method =='POST':

        sp_length=float(request.form.get('sepal_length'))
        sp_width=float(request.form.get('sepal_width'))
        pt_length=float(request.form.get('petal_length'))
        pt_width=float(request.form.get('petal_width'))
        p=predict_flower_class(sp_length,sp_width,pt_length,pt_width)

        
        context={
            'target_name':iris_dataset['target_names'][p][0]
        }
    return render_template('index.html',**context)


