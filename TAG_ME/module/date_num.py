# -*- coding: utf-8 -*-
"""준서.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10AHjTPXRrSwPdM9ehZf-E5PzJxvZrzYo
"""

get_ipython().run_line_magic('matplotlib', 'inline')
from flask import Flask, send_file
from matplotlib import style
from pandas import DataFrame
import pandas as pd
from matplotlib import font_manager, rc
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
from io import BytesIO
import base64
from datetime import datetime
"""**날짜 범위 선정해서 그래프 그리기**"""
    
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 실시간 가능 코드
def date_num():
    # 저장된 해시태그 csv파일
    df = pd.read_csv('hashtag.csv',index_col='date',parse_dates=True)

    df[['Unnamed: 0','tag_total']] = df[['Unnamed: 0','tag_total']].astype(str)
    df['all_news_num'] = 1
    weekly_df = df.resample(rule='1H').sum().fillna(0)
    weekly = weekly_df.reset_index()
    weekly['new_date'] = pd.to_datetime(weekly['date'])
    df1=weekly[-12:]
    df1.rename(columns={'all_news_num':'figure'}, inplace =True)

    x = np.array(df1.new_date)
    y = np.array(df1.figure)

    plt.figure(figsize=(10, 10)) #그래프크기

    plt.title('Hour Expresion', fontsize=20)
    plt.xlabel('Time', fontsize=18)
    plt.ylabel('Figure', fontsize=18)

    plt.bar(df1['new_date'],df1['figure'],width=0.035,alpha = 0.7)

    for i, v in enumerate(x):
        plt.text(v,y[i], y[i],
        fontsize = 15, 
        horizontalalignment='center',
        verticalalignment='bottom')


    plt.grid()    #격자생성
    plt.show()
    plt.savefig('static/dateNum.png')
    plt.close()
    
    # 파이차트_ 게시글 1개 이상인 시간만 표시
    df2 = df1[-6:]
    df2.reset_index(inplace=True)
    df2 = df2.drop(['index','date'], 1)

    ratio = df2['figure']
    labels = df2['new_date']

    group_explodes = [0.02 for i in range(0,len(ratio))]

    colors = ['#F3E5F5', '#E1BEE7', '#CE93D8', '#F48FB1', 
                  '#AB47BC', '#EF9A9A', '#6A1B9A', '#4A148C',
                  '#EA80FC', '#E040FB', '#AA00FF', '#F3E5F5']
    color = [color for color in colors[:len(ratio)]]

    plt.figure(figsize=(15,15))
    plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, 
                textprops={'fontsize': 25}, explode=group_explodes, colors=color)
    
    plt.savefig('static/dateNum_pie.png')
    plt.close()

# 시간이 없는 관계로 만들어진 데이터 사용
def date_num_pl():
    # 저장된 해시태그 csv파일
    df = pd.read_csv('hashtag2.csv',index_col='date',parse_dates=True)

    df[['Unnamed: 0','tag_total']] = df[['Unnamed: 0','tag_total']].astype(str)
    df['all_news_num'] = 1
    weekly_df = df.resample(rule='1H').sum().fillna(0)
    weekly = weekly_df.reset_index()
    weekly['new_date'] = pd.to_datetime(weekly['date'])
    df1=weekly[-12:]
    df1.rename(columns={'all_news_num':'figure'}, inplace =True)

    x = np.array(df1.new_date)
    y = np.array(df1.figure)

    plt.figure(figsize=(10, 10)) #그래프크기

    plt.title('Hour Expresion', fontsize=20)
    plt.xlabel('Time', fontsize=18)
    plt.ylabel('Figure', fontsize=18)

    plt.bar(df1['new_date'],df1['figure'],width=0.035,alpha = 0.7)

    for i, v in enumerate(x):
        plt.text(v,y[i], y[i],
        fontsize = 15, 
        horizontalalignment='center',
        verticalalignment='bottom')


    plt.grid()    #격자생성
    plt.show()
    plt.savefig('static/dateNum.png')
    plt.close()
    
    # 파이차트_ 게시글 1개 이상인 시간만 표시
    df2 = df1[-6:]
    df2.reset_index(inplace=True)
    df2 = df2.drop(['index','date'], 1)

    ratio = df2['figure']
    labels = df2['new_date']

    group_explodes = [0.02 for i in range(0,len(ratio))]

    colors = ['#F3E5F5', '#E1BEE7', '#CE93D8', '#F48FB1', 
                  '#AB47BC', '#EF9A9A', '#6A1B9A', '#4A148C',
                  '#EA80FC', '#E040FB', '#AA00FF', '#F3E5F5']
    color = [color for color in colors[:len(ratio)]]

    plt.figure(figsize=(15,15))
    plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, 
                textprops={'fontsize': 25}, explode=group_explodes, colors=color)
    
    plt.savefig('static/dateNum_pie.png')
    plt.close()
    
def date_num_ham():
    # 저장된 해시태그 csv파일
    df = pd.read_csv('hashtag_ham.csv',index_col='date',parse_dates=True)

    df[['Unnamed: 0','tag_total']] = df[['Unnamed: 0','tag_total']].astype(str)
    df['all_news_num'] = 1
    weekly_df = df.resample(rule='1H').sum().fillna(0)
    weekly = weekly_df.reset_index()
    weekly['new_date'] = pd.to_datetime(weekly['date'])
    df1=weekly[-12:]
    df1.rename(columns={'all_news_num':'figure'}, inplace =True)

    x = np.array(df1.new_date)
    y = np.array(df1.figure)

    plt.figure(figsize=(10, 10)) #그래프크기

    plt.title('Hour Expresion', fontsize=20)
    plt.xlabel('Time', fontsize=18)
    plt.ylabel('Figure', fontsize=18)

    plt.bar(df1['new_date'],df1['figure'],width=0.035,alpha = 0.7)

    for i, v in enumerate(x):
        plt.text(v,y[i], y[i],
        fontsize = 15, 
        horizontalalignment='center',
        verticalalignment='bottom')


    plt.grid()    #격자생성
    plt.show()
    plt.savefig('static/dateNum.png')
    plt.close()
    
    # 파이차트_ 게시글 1개 이상인 시간만 표시
    df2 = df1[-6:]
    df2.reset_index(inplace=True)
    df2 = df2.drop(['index','date'], 1)

    ratio = df2['figure']
    labels = df2['new_date']

    group_explodes = [0.02 for i in range(0,len(ratio))]

    colors = ['#F3E5F5', '#E1BEE7', '#CE93D8', '#F48FB1', 
                  '#AB47BC', '#EF9A9A', '#6A1B9A', '#4A148C',
                  '#EA80FC', '#E040FB', '#AA00FF', '#F3E5F5']
    color = [color for color in colors[:len(ratio)]]

    plt.figure(figsize=(15,15))
    plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, 
                textprops={'fontsize': 25}, explode=group_explodes, colors=color)
    
    plt.savefig('static/dateNum_pie.png')
    plt.close()
    
def date_num_ma():
    # 저장된 해시태그 csv파일
    df = pd.read_csv('hashtag_ma.csv',index_col='date',parse_dates=True)
    df[['Unnamed: 0','tag_total']] = df[['Unnamed: 0','tag_total']].astype(str)
    df['all_news_num'] = 1
    weekly_df = df.resample(rule='1H').sum().fillna(0)
    weekly = weekly_df.reset_index()
    weekly['new_date'] = pd.to_datetime(weekly['date'])
    df1=weekly[-12:]
    df1.rename(columns={'all_news_num':'figure'}, inplace =True)

    x = np.array(df1.new_date)
    y = np.array(df1.figure)

    plt.figure(figsize=(10, 10)) #그래프크기

    plt.title('Hour Expresion', fontsize=20)
    plt.xlabel('Time', fontsize=18)
    plt.ylabel('Figure', fontsize=18)

    plt.bar(df1['new_date'],df1['figure'],width=0.035,alpha = 0.7)

    for i, v in enumerate(x):
        plt.text(v,y[i], y[i],
        fontsize = 15, 
        horizontalalignment='center',
        verticalalignment='bottom')


    plt.grid()    #격자생성

    plt.savefig('static/dateNum.png')
    plt.close()
    
    # 파이차트_ 게시글 1개 이상인 시간만 표시
    df2 = df1[-6:]
    df2.reset_index(inplace=True)
    df2 = df2.drop(['index','date'], 1)

    ratio = df2['figure']
    labels = df2['new_date']

    group_explodes = [0.02 for i in range(0,len(ratio))]

    colors = ['#F3E5F5', '#E1BEE7', '#CE93D8', '#F48FB1', 
                  '#AB47BC', '#EF9A9A', '#6A1B9A', '#4A148C',
                  '#EA80FC', '#E040FB', '#AA00FF', '#F3E5F5']
    color = [color for color in colors[:len(ratio)]]

    plt.figure(figsize=(15,15))
    plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, 
                textprops={'fontsize': 25}, explode=group_explodes, colors=color)
    
    plt.savefig('static/dateNum_pie.png')
    plt.close()