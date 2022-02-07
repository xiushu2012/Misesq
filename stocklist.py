# -*- coding: utf-8 -*-


import pandas as pd  
import math
import datetime
import time
import numpy as np
from collections import Counter
import akshare as ak
import xlsxwriter



def get_hs300_list1():
	index_stock_cons_df = ak.index_stock_cons(index="000300")
	print(index_stock_cons_df)
	
	print(index_stock_cons_df.shape[0])
	#print(index_stock_cons_df['品种代码'].values.tolist()[0:-1])
	hslist = sorted(index_stock_cons_df['品种代码'].values.tolist())
	#[print(index) for index in hslist]
	hsdict = Counter(hslist)
	[print(k,hsdict[k]) for k in hsdict.keys()]
	
def get_hs300_list2():
	index_stock_cons_df = ak.index_stock_cons_sina(index="000300")
	print(index_stock_cons_df)
	
	print(index_stock_cons_df.shape[0])
	#print(index_stock_cons_df['code'].values.tolist()[0:-1])
	hslist = sorted(index_stock_cons_df['code'].values.tolist())
	#[print(index) for index in hslist]
	hsdict = Counter(hslist)
	#[print(k,hsdict[k]) for k in hsdict.keys()]
	[print(k) for k in hsdict.keys()]

def get_hs300_list3():
	index_stock_cons_csindex_df = ak.index_stock_cons_csindex('000300')
	print(index_stock_cons_csindex_df)
	
def get_hs300_history():
	stock_index_hist_df = ak.index_stock_hist(index="sh000300")
	#print(stock_index_hist_df.duplicated())
	#for item in stock_index_hist_df.itertuples():
	#	print(item[1],item[2],item[3])
	stock_index_hist_df= stock_index_hist_df.drop_duplicates()
		
	fileout =  './history300' + '.xlsx'
	writer = pd.ExcelWriter(fileout)
	stock_index_hist_df.to_excel(writer,'his')
	writer.save()
	print("histoy hs300  out in:" + fileout)
		
		
def get_index_code():
	index_stock_info_df = ak.index_stock_info()
	print(index_stock_info_df)


if __name__=='__main__':
	#get_hs300_list2()
	#get_hs300_list3()
	#get_index_code()
	get_hs300_history()
