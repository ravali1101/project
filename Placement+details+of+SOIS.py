import pandas as pd
import hashlib
import numpy as np


# ### read excel sheet


sheet1= pd.read_excel('placements-sois.xlsx',sheetname='PlacementStats')


sheet2= pd.read_excel('placements-sois.xlsx',sheetname='Enrollment')


sheet1_reindexing=sheet1.reset_index()


# ### create data frames for placements sheet

df1=sheet1_reindexing[2:14]
df1.columns = df1.iloc[0]
df1=df1.reindex(df1.index.drop(2))
df1['year_intake']= 2015
df1=df1.ix[:,1:13]
df1=df1.reindex(df1.index.delete(8))
df1.columns = ['Branches','Class Strength_1','# of placed students_1','Self Placement_1','Class Strength_8','# of placed students_8','Self Placement_8','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df1.columns
df1 = df1.reset_index()
del df1['index']


df2=sheet1_reindexing[18:30]
df2.columns = df2.iloc[0]
df2=df2.reindex(df2.index.drop(18))
df2['year_intake']= 2014
df2=df2.ix[:,1:13]
df2 = df2.reset_index()
del df2['index']
df2=df2.reindex(df2.index.delete(7))
df2.columns = ['Branches','Class Strength_1','# of placed students_1','Self Placement','Class Strength_8','# of placed students_8','Self Placement','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df2.columns
df2=df2.drop("Self Placement",axis=1)
df2 = df2.reset_index()
del df2['index']


df3=sheet1_reindexing[34:45]
df3.columns = df3.iloc[0]
df3=df3.reindex(df3.index.drop(34))
df3['year_intake']= 2013
df3=df3.ix[:,1:13]
df3 = df3.reset_index()
del df3['index']
df3.columns = ['Branches','Class Strength_1','# of placed students_1','Self Placement','Class Strength_8','# of placed students_8','Self Placement','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df3.columns
df3.loc[8,'Class Strength_1'] = 32
df3.loc[8,'# of placed students_1'] = 30
df3.loc[8,'Class Strength_8'] = 151
df3.loc[8,'# of placed students_8'] = 146
df3.drop([9])
df3=df3.drop("Self Placement",axis=1)
df3 = df3.reset_index()
del df3['index']


df4=sheet1_reindexing[50:61]
df4.columns = df4.iloc[0]
df4=df4.reindex(df4.index.drop(50))
df4['year_intake']= 2012
df4 = df4.reset_index()
del df4['index']
df4.columns = ['nan1','Branches','Class Strength_1','# of placed students_1','Self Placement','Class Strength_8','# of placed students_8','Self Placement','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df4.columns
df4=df4.drop("Self Placement",axis=1)
df4=df4.drop("nan1",axis=1)
df4 = df4.reset_index()
del df4['index']
df5=sheet1_reindexing[66:77]
df5.columns = df5.iloc[0]
df5=df5.reindex(df5.index.drop(66))
df5['year_intake']= 2011
df5 = df5.reset_index()
del df5['index']
df5.columns = ['nan1','Branches','Class Strength_1','# of placed students_1','Self Placement','Class Strength_8','# of placed students_8','Self Placement','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df5=df5.drop("Self Placement",axis=1)
df5=df5.drop("nan1",axis=1)
df5 = df5.reset_index()
del df5['index']


df6=sheet1_reindexing[83:92]
df6.columns = df6.iloc[0]
df6=df6.reindex(df6.index.drop(83))
df6['year_intake']= 2010
df6 = df6.reset_index()
del df6['index']
df6.columns = ['nan1','Branches','Class Strength_1','# of placed students_1','Self Placement','Class Strength_8','# of placed students_8','Self Placement','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df6=df6.drop("Self Placement",axis=1)
df6=df6.drop("nan1",axis=1)
df6 = df6.reset_index()
del df6['index']


df7=sheet1_reindexing[98:106]
df7.columns = df7.iloc[0]
df7=df7.reindex(df7.index.drop(98))
df7['year_intake']= 2009
df7 = df7.reset_index()
del df7['index']
df7.columns = ['nan1','Branches','Class Strength_1','# of placed students_1','Self Placement','Class Strength_8','# of placed students_8','Self Placement','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df7=df7.drop("Self Placement",axis=1)
df7=df7.drop("nan1",axis=1)
df7 = df7.reset_index()
del df7['index']


df8=sheet1_reindexing[112:120]
df8.columns = df8.iloc[0]
df8=df8.reindex(df8.index.drop(112))
df8['year_intake']= 2008
df8 = df8.reset_index()
del df8['index']
df8.columns = ['nan1','Branches','Class Strength_1','# of placed students_1','Self Placement','Class Strength_8','# of placed students_8','Self Placement','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df8=df8.drop("Self Placement",axis=1)
df8=df8.drop("nan1",axis=1)
df8 = df8.reset_index()
del df8['index']


df9=sheet1_reindexing[126:133]
df9.columns = df9.iloc[0]
df9=df9.reindex(df9.index.drop(126))
df9['year_intake']= 2007
df9 = df9.reset_index()
del df9['index']
df9.columns = ['nan1','Branches','Class Strength_1','# of placed students_1','Self Placement','Class Strength_8','# of placed students_8','Self Placement','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df9=df9.drop("Self Placement",axis=1)
df9=df9.drop("nan1",axis=1)


df10=sheet1_reindexing[138:145]
df10.columns = df10.iloc[0]
df10=df10.reindex(df10.index.drop(138))
df10['year_intake']= 2006
df10 = df10.reset_index()
del df10['index']
df10.columns = ['nan1','Branches','Class Strength_1','# of placed students_1','Self Placement','Class Strength_8','# of placed students_8','Self Placement','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df10=df10.drop("Self Placement",axis=1)
df10=df10.drop("nan1",axis=1)


df11=sheet1_reindexing[150:155]
df11.columns = df11.iloc[0]
df11=df11.reindex(df11.index.drop(150))
df11['year_intake']= 2005
df11 = df11.reset_index()
del df11['index']
df11.columns = ['nan1','Branches','Class Strength_1','# of placed students_1','Self Placement','Class Strength_8','# of placed students_8','Self Placement','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df11=df11.drop("Self Placement",axis=1)
df11=df11.drop("nan1",axis=1)


df12=sheet1_reindexing[160:165]
df12.columns = df12.iloc[0]
df12=df12.reindex(df12.index.drop(160))
df12['year_intake']= 2004
df12 = df12.reset_index()
del df12['index']
df12.columns = ['nan1','Branches','Class Strength_1','# of placed students_1','Self Placement','Class Strength_8','# of placed students_8','Self Placement','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df12=df12.drop("Self Placement",axis=1)
df12=df12.drop("nan1",axis=1)


df13=sheet1_reindexing[170:176]
df13.columns = df13.iloc[0]
df13=df13.reindex(df13.index.drop(170))
df13['year_intake']= 2003
df13 = df13.reset_index()
del df13['index']
df13.columns = ['nan1','Branches','Class Strength_1','# of placed students_1','Self Placement','Class Strength_8','# of placed students_8','Self Placement','Class Strength','# of placed students','Self Placement','Total placement %','year_intake']
df13=df13.drop("Self Placement",axis=1)
df13=df13.drop("nan1",axis=1)


# ### create data frames for enrollment sheet



enroll_1=sheet2[3:35]
enroll_1.loc[:,'year'] = 'Aug 1999 to Feb 2001'
enroll_1['Batch']='Batch_1'
enroll_1['Branch']='MS Ecommerce'
enroll_1.columns = enroll_1.iloc[0]
enroll_1=enroll_1.reindex(enroll_1.index.drop(3))
enroll_1 = enroll_1.reset_index()
del enroll_1['index']
enroll_1.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_1=enroll_1.drop("nan",axis=1)
enroll_1=enroll_1.set_index('NO')


enroll_2=sheet2[35:47]
enroll_2.loc[:,'year'] = ' Feb 2000 to Aug 2001'
enroll_2['Batch']='Batch_2'
enroll_2['Branch']='MS Ecommerce'
enroll_2.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_2=enroll_2.reindex(enroll_2.index.drop(35))
enroll_2 = enroll_2.reset_index()
del enroll_2['index']
enroll_2=enroll_2.drop("nan",axis=1)
enroll_2=enroll_2.set_index('NO')
enroll_2.to_csv('enroll.csv')


enroll_3=sheet2[47:72]
enroll_3.loc[:,'year'] = 'Aug 2000 to Feb 2002'
enroll_3['Batch']='Batch_3'
enroll_3['Branch']='MS Ecommerce'
enroll_3.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_3=enroll_3.reindex(enroll_3.index.drop(47))
enroll_3 = enroll_3.reset_index()
del enroll_3['index']
enroll_3=enroll_3.drop("nan",axis=1)
enroll_3=enroll_3.set_index('NO')


enroll_4=sheet2[73:78]
enroll_4.loc[:,'year'] = 'Feb 2001 to Aug 2002'
enroll_4['Batch']='Batch_4'
enroll_4['Branch']='MS Ecommerce'
enroll_4.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_4 = enroll_4.reset_index()
del enroll_4['index']
enroll_4=enroll_4.drop("nan",axis=1)
enroll_4=enroll_4.set_index('NO')


enroll_5=sheet2[79:84]
enroll_5.loc[:,'year'] = 'Aug 2001 to Feb 2003'
enroll_5['Batch']='Batch_5'
enroll_5['Branch']='MS Ecommerce'
enroll_5.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_5 = enroll_5.reset_index()
del enroll_5['index']
enroll_5=enroll_5.drop("nan",axis=1)
enroll_5=enroll_5.set_index('NO')


enroll_6=sheet2[87:102]
enroll_6.loc[:,'year'] = 'Aug 1998 to Feb 2000'
enroll_6['Batch']='Batch_1'
enroll_6['Branch']='MS MEDICAL SOFTWARE'
enroll_6.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_6 = enroll_6.reset_index()
del enroll_6['index']
enroll_6=enroll_6.drop("nan",axis=1)
enroll_6=enroll_6.set_index('NO')


enroll_7=sheet2[103:113]
enroll_7.loc[:,'year'] = 'Feb 1999 to Aug 2000'
enroll_7['Batch']='Batch_2'
enroll_7['Branch']='MS MEDICAL SOFTWARE'
enroll_7.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_7 = enroll_7.reset_index()
del enroll_7['index']
enroll_7=enroll_7.drop("nan",axis=1)
enroll_7=enroll_7.set_index('NO')


enroll_8=sheet2[114:124]
enroll_8.loc[:,'year'] = 'Aug 1999 to Feb 2001'
enroll_8['Batch']='Batch_3'
enroll_8['Branch']='MS MEDICAL SOFTWARE'
enroll_8.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_8 = enroll_8.reset_index()
del enroll_8['index']
enroll_8=enroll_8.drop("nan",axis=1)
enroll_8=enroll_8.set_index('NO')


enroll_9=sheet2[125:132]
enroll_9.loc[:,'year'] = 'Aug 2000 to Feb 2002'
enroll_9['Batch']='Batch_4'
enroll_9['Branch']='MS MEDICAL SOFTWARE'
enroll_9.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_9 = enroll_9.reset_index()
del enroll_9['index']
enroll_9=enroll_9.drop("nan",axis=1)
enroll_9=enroll_9.set_index('NO')


enroll_10=sheet2[133:150]
enroll_10.loc[:,'year'] = 'Aug 2001 to Feb 2003'
enroll_10['Batch']='Batch_5'
enroll_10['Branch']='MS MEDICAL SOFTWARE'
enroll_10.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_10 = enroll_10.reset_index()
del enroll_10['index']
enroll_10=enroll_10.drop("nan",axis=1)
enroll_10=enroll_10.set_index('NO')


enroll_11=sheet2[151:166]
enroll_11.loc[:,'year'] = 'Feb 2002 to Aug 2003'
enroll_11['Batch']='Batch_6'
enroll_11['Branch']='MS MEDICAL SOFTWARE'
enroll_11.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_11 = enroll_11.reset_index()
del enroll_11['index']
enroll_11=enroll_11.drop("nan",axis=1)
enroll_11=enroll_11.set_index('NO')


enroll_12=sheet2[167:172]
enroll_12.loc[:,'year'] = 'Aug 2002 to Feb 2004'
enroll_12['Batch']='Batch_7'
enroll_12['Branch']='MS MEDICAL SOFTWARE'
enroll_12.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_12 = enroll_12.reset_index()
del enroll_12['index']
enroll_12=enroll_12.drop("nan",axis=1)
enroll_12=enroll_12.set_index('NO')


enroll_13=sheet2[173:189]
enroll_13.loc[:,'year'] = 'Feb 2003 to Feb 2005'
enroll_13['Batch']='Batch_8'
enroll_13['Branch']='MS MEDICAL SOFTWARE'
enroll_13.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_13 = enroll_13.reset_index()
del enroll_13['index']
enroll_13=enroll_13.drop("nan",axis=1)
enroll_13=enroll_13.set_index('NO')


enroll_14=sheet2[190:206]
enroll_14.loc[:,'year'] = 'Aug 2003 to Aug 2005'
enroll_14['Batch']='Batch_9'
enroll_14['Branch']='MS MEDICAL SOFTWARE'
enroll_14.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_14 = enroll_14.reset_index()
del enroll_14['index']
enroll_14=enroll_14.drop("nan",axis=1)
enroll_14=enroll_14.set_index('NO')


enroll_15=sheet2[207:213]
enroll_15.loc[:,'year'] = 'Feb 2004 to Feb 2006'
enroll_15['Batch']='Batch_10'
enroll_15['Branch']='MS MEDICAL SOFTWARE'
enroll_15.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_15 = enroll_15.reset_index()
del enroll_15['index']
enroll_15=enroll_15.drop("nan",axis=1)
enroll_15=enroll_15.set_index('NO')


enroll_16=sheet2[214:224]
enroll_16.loc[:,'year'] = 'Aug 2004 to Aug 2006'
enroll_16['Batch']='Batch_11'
enroll_16['Branch']='MS MEDICAL SOFTWARE'
enroll_16.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_16 = enroll_16.reset_index()
del enroll_16['index']
enroll_16=enroll_16.drop("nan",axis=1)
enroll_16=enroll_16.set_index('NO')


enroll_17=sheet2[225:237]
enroll_17.loc[:,'year'] = 'Aug 2005 to Aug 2007'
enroll_17['Batch']='Batch_12'
enroll_17['Branch']='MS MEDICAL SOFTWARE'
enroll_17.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_17 = enroll_17.reset_index()
del enroll_17['index']
enroll_17=enroll_17.drop("nan",axis=1)
enroll_17=enroll_17.set_index('NO')


enroll_18=sheet2[238:261]
enroll_18.loc[:,'year'] = 'Aug 2006 to Jul 2008'
enroll_18['Batch']='Batch_13'
enroll_18['Branch']='MS MEDICAL SOFTWARE'
enroll_18.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_18 = enroll_18.reset_index()
del enroll_18['index']
enroll_18=enroll_18.drop("nan",axis=1)
enroll_18=enroll_18.set_index('NO')


enroll_19=sheet2[262:269]
enroll_19.loc[:,'year'] = 'Jan 2007 to Dec 2008'
enroll_19['Batch']='Batch_14'
enroll_19['Branch']='MS MEDICAL SOFTWARE'
enroll_19.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_19 = enroll_19.reset_index()
del enroll_19['index']
enroll_19=enroll_19.drop("nan",axis=1)
enroll_19=enroll_19.set_index('NO')


enroll_20=sheet2[270:288]
enroll_20.loc[:,'year'] = 'Aug 2007 to July 2009'
enroll_20['Batch']='Batch_15'
enroll_20['Branch']='MS MEDICAL SOFTWARE'
enroll_20.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_20 = enroll_20.reset_index()
del enroll_20['index']
enroll_20=enroll_20.drop("nan",axis=1)
enroll_20=enroll_20.set_index('NO')


enroll_21=sheet2[289:291]
enroll_21.loc[:,'year'] = 'Jan 2008 to Dec 2009'
enroll_21['Batch']='Batch_16'
enroll_21['Branch']='MS MEDICAL SOFTWARE'
enroll_21.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_21 = enroll_21.reset_index()
del enroll_21['index']
enroll_21=enroll_21.drop("nan",axis=1)
enroll_21=enroll_21.set_index('NO')


enroll_22=sheet2[292:317]
enroll_22.loc[:,'year'] = 'Aug 2008 to July 2010'
enroll_22['Batch']='Batch_17'
enroll_22['Branch']='MS MEDICAL SOFTWARE'
enroll_22.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_22 = enroll_22.reset_index()
del enroll_22['index']
enroll_22=enroll_22.drop("nan",axis=1)
enroll_22=enroll_22.set_index('NO')


enroll_23=sheet2[318:328]
enroll_23.loc[:,'year'] = 'Jan 2009 to Dec 2010'
enroll_23['Batch']='Batch_18'
enroll_23['Branch']='MS MEDICAL SOFTWARE'
enroll_23.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_23 = enroll_23.reset_index()
del enroll_23['index']
enroll_23=enroll_23.drop("nan",axis=1)
enroll_23=enroll_23.set_index('NO')


enroll_24=sheet2[329:355]
enroll_24.loc[:,'year'] = 'Aug 09 to July 2011'
enroll_24['Batch']='Batch_19'
enroll_24['Branch']='MS MEDICAL SOFTWARE'
enroll_24.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_24 = enroll_24.reset_index()
del enroll_24['index']
enroll_24=enroll_24.drop("nan",axis=1)
enroll_24=enroll_24.set_index('NO')


enroll_25=sheet2[356:361]
enroll_25.loc[:,'year'] = 'Jan 2010 to Dec 2011'
enroll_25['Batch']='Batch_20'
enroll_25['Branch']='MS MEDICAL SOFTWARE'
enroll_25.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_25 = enroll_25.reset_index()
del enroll_25['index']
enroll_25=enroll_25.drop("nan",axis=1)
enroll_25=enroll_25.set_index('NO')


enroll_26=sheet2[362:392]
enroll_26.loc[:,'year'] = 'Aug 10 to July 2012'
enroll_26['Batch']='Batch_21'
enroll_26['Branch']='MS MEDICAL SOFTWARE'
enroll_26.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_26 = enroll_26.reset_index()
del enroll_26['index']
enroll_26=enroll_26.drop("nan",axis=1)
enroll_26=enroll_26.set_index('NO')


enroll_27=sheet2[393:415]
enroll_27.loc[:,'year'] = 'Aug 11 to July 2013'
enroll_27['Batch']='Batch_21'
enroll_27['Branch']='MS MEDICAL SOFTWARE'
enroll_27.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_27 = enroll_27.reset_index()
del enroll_27['index']
enroll_27=enroll_27.drop("nan",axis=1)
enroll_27=enroll_27.set_index('NO')


enroll_53=sheet2[968:989]
enroll_53.loc[:,'year'] = 'Aug 2002 to Feb 2004'
enroll_53['Batch']='Batch_1'
enroll_53['Branch']='MS EMBEDDED SYSTEMS'
enroll_53.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_53 = enroll_53.reset_index()
del enroll_53['index']
enroll_53=enroll_53.drop("nan",axis=1)
enroll_53=enroll_53.set_index('NO')


enroll_54=sheet2[990:1000]
enroll_54.loc[:,'year'] = 'Feb 2003 to Feb 2005'
enroll_54['Batch']='Batch_2'
enroll_54['Branch']='MS EMBEDDED SYSTEMS'
enroll_54.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_54 = enroll_54.reset_index()
del enroll_54['index']
enroll_54=enroll_54.drop("nan",axis=1)
enroll_54=enroll_54.set_index('NO')


enroll_55=sheet2[1001:1031]
enroll_55.loc[:,'year'] = 'Aug 2003 to Jul 2005'
enroll_55['Batch']='Batch_3'
enroll_55['Branch']='MS EMBEDDED SYSTEMS'
enroll_55.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_55 = enroll_55.reset_index()
del enroll_55['index']
enroll_55=enroll_55.drop("nan",axis=1)
enroll_55=enroll_55.set_index('NO')


enroll_56=sheet2[1032:1040]
enroll_56.loc[:,'year'] = 'Feb 2004 to Jan 2006'
enroll_56['Batch']='Batch_4'
enroll_56['Branch']='MS EMBEDDED SYSTEMS'
enroll_56.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_56 = enroll_56.reset_index()
del enroll_56['index']
enroll_56=enroll_56.drop("nan",axis=1)
enroll_56=enroll_56.set_index('NO')


enroll_57=sheet2[1041:1061]
enroll_57.loc[:,'year'] = 'Aug 2004 to Jul 2006'
enroll_57['Batch']='Batch_5'
enroll_57['Branch']='MS EMBEDDED SYSTEMS'
enroll_57.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_57 = enroll_57.reset_index()
del enroll_57['index']
enroll_57=enroll_57.drop("nan",axis=1)
enroll_57=enroll_57.set_index('NO')


enroll_58=sheet2[1062:1073]
enroll_58.loc[:,'year'] = 'Feb 2005 to Jan  2007'
enroll_58['Batch']='Batch_6'
enroll_58['Branch']='MS EMBEDDED SYSTEMS'
enroll_58.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_58 = enroll_58.reset_index()
del enroll_58['index']
enroll_58=enroll_58.drop("nan",axis=1)
enroll_58=enroll_58.set_index('NO')


enroll_59=sheet2[1074:1113]
enroll_59.loc[:,'year'] = 'Aug 2005 to Jul  2007'
enroll_59['Batch']='Batch_7'
enroll_59['Branch']='MS EMBEDDED SYSTEMS'
enroll_59.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_59 = enroll_59.reset_index()
del enroll_59['index']
enroll_59=enroll_59.drop("nan",axis=1)
enroll_59=enroll_59.set_index('NO')


enroll_60=sheet2[1114:1136]
enroll_60.loc[:,'year'] = 'Jan 2006 to Dec 2007'
enroll_60['Batch']='Batch_8'
enroll_60['Branch']='MS EMBEDDED SYSTEMS'
enroll_60.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_60 = enroll_60.reset_index()
del enroll_60['index']
enroll_60=enroll_60.drop("nan",axis=1)
enroll_60=enroll_60.set_index('NO')


enroll_61=sheet2[1137:1187]
enroll_61.loc[:,'year'] = 'Aug 2006 July 2008'
enroll_61['Batch']='Batch_9'
enroll_61['Branch']='MS EMBEDDED SYSTEMS'
enroll_61.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_61 = enroll_61.reset_index()
del enroll_61['index']
enroll_61=enroll_61.drop("nan",axis=1)
enroll_61=enroll_61.set_index('NO')


enroll_62=sheet2[1188:1217]
enroll_62.loc[:,'year'] = 'Jan 2007 to Dec 2008'
enroll_62['Batch']='Batch_10'
enroll_62['Branch']='MS EMBEDDED SYSTEMS'
enroll_62.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_62 = enroll_62.reset_index()
del enroll_62['index']
enroll_62=enroll_62.drop("nan",axis=1)
enroll_62=enroll_62.set_index('NO')


enroll_63=sheet2[1218:1309]
enroll_63.loc[:,'year'] = 'Aug 2007 to Jul 2009'
enroll_63['Batch']='Batch_11'
enroll_63['Branch']='MS EMBEDDED SYSTEMS'
enroll_63.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_63 = enroll_63.reset_index()
del enroll_63['index']
enroll_63=enroll_63.drop("nan",axis=1)
enroll_63=enroll_63.set_index('NO')


enroll_64=sheet2[1310:1330]
enroll_64.loc[:,'year'] = 'Jan 2008 to Dec 2009'
enroll_64['Batch']='Batch_12'
enroll_64['Branch']='MS EMBEDDED SYSTEMS'
enroll_64.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_64 = enroll_64.reset_index()
del enroll_64['index']
enroll_64=enroll_64.drop("nan",axis=1)
enroll_64=enroll_64.set_index('NO')


enroll_65=sheet2[1331:1425]
enroll_65.loc[:,'year'] = 'Aug 2008 to July2010'
enroll_65['Batch']='Batch_13'
enroll_65['Branch']='MS EMBEDDED SYSTEMS'
enroll_65.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_65 = enroll_65.reset_index()
del enroll_65['index']
enroll_65=enroll_65.drop("nan",axis=1)
enroll_65=enroll_65.set_index('NO')


enroll_66=sheet2[1428:1435]
enroll_66.loc[:,'year'] = 'Jan 2009 to Dec 2010'
enroll_66['Batch']='Batch_14'
enroll_66['Branch']='MS EMBEDDED SYSTEMS'
enroll_66.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_66 = enroll_66.reset_index()
del enroll_66['index']
enroll_66=enroll_66.drop("nan",axis=1)
enroll_66=enroll_66.set_index('NO')


enroll_67=sheet2[1436:1570]
enroll_67.loc[:,'year'] = 'Aug 2009 to July 2011'
enroll_67['Batch']='Batch_15'
enroll_67['Branch']='MS EMBEDDED SYSTEMS'
enroll_67.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_67 = enroll_67.reset_index()
del enroll_67['index']
enroll_67=enroll_67.drop("nan",axis=1)
enroll_67=enroll_67.set_index('NO')


enroll_68=sheet2[1571:1623]
enroll_68.loc[:,'year'] = 'Jan 2010 to Dec 2011'
enroll_68['Batch']='Batch_16'
enroll_68['Branch']='MS EMBEDDED SYSTEMS'
enroll_68.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_68 = enroll_68.reset_index()
del enroll_68['index']
enroll_68=enroll_68.drop("nan",axis=1)
enroll_68=enroll_68.set_index('NO')


enroll_69=sheet2[1626:1706]
enroll_69.loc[:,'year'] = 'Aug 2010 to Jul 2012'
enroll_69['Batch']='Batch_17'
enroll_69['Branch']='MS EMBEDDED SYSTEMS'
enroll_69.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_69 = enroll_69.reset_index()
del enroll_69['index']
enroll_69=enroll_69.drop("nan",axis=1)
enroll_69=enroll_69.set_index('NO')


enroll_70=sheet2[1709:1759]
enroll_70.loc[:,'year'] = 'Jan 2011 to Dec 2012'
enroll_70['Batch']='Batch_18'
enroll_70['Branch']='MS EMBEDDED SYSTEMS'
enroll_70.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_70 = enroll_70.reset_index()
del enroll_70['index']
enroll_70=enroll_70.drop("nan",axis=1)
enroll_70=enroll_70.set_index('NO')


enroll_71=sheet2[1762:1842]
enroll_71.loc[:,'year'] = 'Aug 2011 to Jul 2013'
enroll_71['Batch']='Batch_19'
enroll_71['Branch']='MS EMBEDDED SYSTEMS'
enroll_71.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_71 = enroll_71.reset_index()
del enroll_71['index']
enroll_71=enroll_71.drop("nan",axis=1)
enroll_71=enroll_71.set_index('NO')


enroll_72=sheet2[1861:1891]
enroll_72.loc[:,'year'] = 'Aug 2010 to Jul 2012'
enroll_72['Batch']='Batch_1'
enroll_72['Branch']=' MS Embedded & Wireless Technology '
enroll_72.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_72 = enroll_72.reset_index()
del enroll_72['index']
enroll_72=enroll_72.drop("nan",axis=1)
enroll_72=enroll_72.set_index('NO')


enroll_73=sheet2[1894:1909]
enroll_73.loc[:,'year'] = 'JAN 2011 to DEC 2012'
enroll_73['Batch']='Batch_2'
enroll_73['Branch']=' MS Embedded & Wireless Technology '
enroll_73.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_73 = enroll_73.reset_index()
del enroll_73['index']
enroll_73=enroll_73.drop("nan",axis=1)
enroll_73=enroll_73.set_index('NO')


enroll_74=sheet2[1912:1942]
enroll_74.loc[:,'year'] = 'Aug 2011 to Jul 2013'
enroll_74['Batch']='Batch_3'
enroll_74['Branch']=' MS Embedded & Wireless Technology '
enroll_74.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_74 = enroll_74.reset_index()
del enroll_74['index']
enroll_74=enroll_74.drop("nan",axis=1)
enroll_74=enroll_74.set_index('NO')


enroll_85=sheet2[2186:2223]
enroll_85.loc[:,'year'] = 'Jan 2012 to Dec  2013'
enroll_85['Batch']='Batch_1'
enroll_85['Branch']=' MSc Tech Embedded Systems '
enroll_85.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_85 = enroll_85.reset_index()
del enroll_85['index']
enroll_85=enroll_85.drop("nan",axis=1)
enroll_85=enroll_85.set_index('NO')


enroll_86=sheet2[2226:2237]
enroll_86.loc[:,'year'] = 'Jan 2012 to Dec  2013'
enroll_86['Batch']='Batch_1'
enroll_86['Branch']=' MSc Tech VLSI DESIGN  '
enroll_86.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_86 = enroll_86.reset_index()
del enroll_86['index']
enroll_86=enroll_86.drop("nan",axis=1)
enroll_86=enroll_86.set_index('NO')


enroll_87=sheet2[2257:2262]
enroll_87.loc[:,'year'] = 'Aug 2000 to Jul 2001'
enroll_87['Batch']='Batch_1'
enroll_87['Branch']='PG DIPLOMA IN E-COMMERCE'
enroll_87.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_87 = enroll_87.reset_index()
del enroll_87['index']
enroll_87=enroll_87.drop("nan",axis=1)
enroll_87=enroll_87.set_index('NO')


enroll_88=sheet2[2264:2270]
enroll_88.loc[:,'year'] = 'Aug 2001 to Jul 2004'
enroll_88['Batch']='Batch_1'
enroll_88['Branch']='BACHELOR OF COMPUTER APPLICATION'
enroll_88.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_88 = enroll_88.reset_index()
del enroll_88['index']
enroll_88=enroll_88.drop("nan",axis=1)
enroll_88=enroll_88.set_index('NO')


enroll_89=sheet2[2271:2276]
enroll_89.loc[:,'year'] = 'Aug 2002 to Jul 2005'
enroll_89['Batch']='Batch_2'
enroll_89['Branch']='BACHELOR OF COMPUTER APPLICATION'
enroll_89.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_89 = enroll_89.reset_index()
del enroll_89['index']
enroll_89=enroll_89.drop("nan",axis=1)
enroll_89=enroll_89.set_index('NO')


enroll_90=sheet2[2277:2285]
enroll_90.loc[:,'year'] = 'Aug 2003 to Jul 2006'
enroll_90['Batch']='Batch_3'
enroll_90['Branch']='BACHELOR OF COMPUTER APPLICATION'
enroll_90.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_90 = enroll_90.reset_index()
del enroll_90['index']
enroll_90=enroll_90.drop("nan",axis=1)
enroll_90=enroll_90.set_index('NO')


enroll_91=sheet2[2288:2308]
enroll_91.loc[:,'year'] = 'Aug 2005 to July 2007'
enroll_91['Batch']='Batch_1'
enroll_91['Branch']='MSc DIGITAL DESIGN & EMBEDDED SYSTEMS'
enroll_91.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_91 = enroll_91.reset_index()
del enroll_91['index']
enroll_91=enroll_91.drop("nan",axis=1)
enroll_91=enroll_91.set_index('NO')


enroll_92=sheet2[2309:2327]
enroll_92.loc[:,'year'] = 'Aug 2006 to July 2008'
enroll_92['Batch']='Batch_2'
enroll_92['Branch']='MSc DIGITAL DESIGN & EMBEDDED SYSTEMS'
enroll_92.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_92 = enroll_92.reset_index()
del enroll_92['index']
enroll_92=enroll_92.drop("nan",axis=1)
enroll_92=enroll_92.set_index('NO')
list1=[7,8,12,13,16,17]
for i in range(0,6):
    enroll_92=enroll_92.drop(list1[i],axis=0)
enroll_92.index=range(1,13)


enroll_93=sheet2[2328:2340]
enroll_93.loc[:,'year'] = 'Aug 2007 to July 2009'
enroll_93['Batch']='Batch_3'
enroll_93['Branch']='MSc DIGITAL DESIGN & EMBEDDED SYSTEMS'
enroll_93.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_93 = enroll_93.reset_index()
del enroll_93['index']
enroll_93=enroll_93.drop("nan",axis=1)
enroll_93=enroll_93.set_index('NO')


enroll_94=sheet2[2341:2355]
enroll_94.loc[:,'year'] = 'Aug 2008 to July 2010'
enroll_94['Batch']='Batch_4'
enroll_94['Branch']='MSc DIGITAL DESIGN & EMBEDDED SYSTEMS'
enroll_94.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_94 = enroll_94.reset_index()
del enroll_94['index']
enroll_94=enroll_94.drop("nan",axis=1)
enroll_94=enroll_94.set_index('NO')


enroll_95=sheet2[2356:2363]
enroll_95.loc[:,'year'] = 'Aug 2009 to July 2011'
enroll_95['Batch']='Batch_5'
enroll_95['Branch']='MSc DIGITAL DESIGN & EMBEDDED SYSTEMS'
enroll_95.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_95 = enroll_95.reset_index()
del enroll_95['index']
enroll_95=enroll_95.drop("nan",axis=1)
enroll_95=enroll_95.set_index('NO')


enroll_96=sheet2[2366:2374]
enroll_96.loc[:,'year'] = 'Aug 2010 to Jul 2012'
enroll_96['Batch']='Batch_6'
enroll_96['Branch']='MSc DIGITAL DESIGN & EMBEDDED SYSTEMS'
enroll_96.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_96 = enroll_96.reset_index()
del enroll_96['index']
enroll_96=enroll_96.drop("nan",axis=1)
enroll_96=enroll_96.set_index('NO')


enroll_97=sheet2[2377:2382]
enroll_97.loc[:,'year'] = 'Aug 2011 to Jul 2013'
enroll_97['Batch']='Batch_7'
enroll_97['Branch']='MSc DIGITAL DESIGN & EMBEDDED SYSTEMS'
enroll_97.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_97 = enroll_97.reset_index()
del enroll_97['index']
enroll_97=enroll_97.drop("nan",axis=1)
enroll_97=enroll_97.set_index('NO')


enroll_98=sheet2[2441:2445]
enroll_98.loc[:,'year'] = 'Aug 2005 to Jul 2007'
enroll_98['Batch']='Batch_1'
enroll_98['Branch']='MSc INFORMATION SCIENCE'
enroll_98.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_98 = enroll_98.reset_index()
del enroll_98['index']
enroll_98=enroll_98.drop("nan",axis=1)
enroll_98=enroll_98.set_index('NO')


enroll_99=sheet2[2446:2453]
enroll_99.loc[:,'year'] = 'Aug 2006 to Jul 2008'
enroll_99['Batch']='Batch_2'
enroll_99['Branch']='MSc INFORMATION SCIENCE'
enroll_99.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_99 = enroll_99.reset_index()
del enroll_99['index']
enroll_99=enroll_99.drop("nan",axis=1)
enroll_99=enroll_99.set_index('NO')


enroll_100=sheet2[2454:2460]
enroll_100.loc[:,'year'] = 'Aug 2007 to Jul 2009'
enroll_100['Batch']='Batch_3'
enroll_100['Branch']='MSc INFORMATION SCIENCE'
enroll_100.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_100 = enroll_100.reset_index()
del enroll_100['index']
enroll_100=enroll_100.drop("nan",axis=1)
enroll_100=enroll_100.set_index('NO')


enroll_101=sheet2[2461:2470]
enroll_101.loc[:,'year'] = 'Aug 2008 to Jul 2010'
enroll_101['Batch']='Batch_4'
enroll_101['Branch']='MSc INFORMATION SCIENCE'
enroll_101.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_101 = enroll_101.reset_index()
del enroll_101['index']
enroll_101=enroll_101.drop("nan",axis=1)
enroll_101=enroll_101.set_index('NO')


enroll_102=sheet2[2471:2479]
enroll_102.loc[:,'year'] = 'Aug 2009 to Jul 2011'
enroll_102['Batch']='Batch_5'
enroll_102['Branch']='MSc INFORMATION SCIENCE'
enroll_102.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_102 = enroll_102.reset_index()
del enroll_102['index']
enroll_102=enroll_102.drop("nan",axis=1)
enroll_102=enroll_102.set_index('NO')


enroll_103=sheet2[2481:2501]
enroll_103.loc[:,'year'] = 'Aug 2010 to Jul 2012'
enroll_103['Batch']='Batch_6'
enroll_103['Branch']='MSc INFORMATION SCIENCE'
enroll_103.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_103 = enroll_103.reset_index()
del enroll_103['index']
enroll_103=enroll_103.drop("nan",axis=1)
enroll_103=enroll_103.set_index('NO')


enroll_104=sheet2[2502:2519]
enroll_104.loc[:,'year'] = 'Aug 2011 to Jul 2013'
enroll_104['Batch']='Batch_7'
enroll_104['Branch']='MSc INFORMATION SCIENCE'
enroll_104.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_104 = enroll_104.reset_index()
del enroll_104['index']
enroll_104=enroll_104.drop("nan",axis=1)
enroll_104=enroll_104.set_index('NO')


enroll_105=sheet2[2534:2539]
enroll_105.loc[:,'year'] = 'Aug 2007 to Jul 2009'
enroll_105['Batch']='Batch_1'
enroll_105['Branch']='MSc WEB COMMERCE'
enroll_105.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_105 = enroll_105.reset_index()
del enroll_105['index']
enroll_105=enroll_105.drop("nan",axis=1)
enroll_105=enroll_105.set_index('NO')


enroll_28=sheet2[447:458]
enroll_28.loc[:,'year'] = 'Aug 1999 to Feb 2001'
enroll_28['Batch']='Batch_1'
enroll_28['Branch']='MS VLSI-CAD'
enroll_28.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_28 = enroll_28.reset_index()
del enroll_28['index']
enroll_28=enroll_28.drop("nan",axis=1)
enroll_28=enroll_28.set_index('NO')


enroll_29=sheet2[459:466]
enroll_29.loc[:,'year'] = 'Feb 2000 to Aug 2001'
enroll_29['Batch']='Batch_2'
enroll_29['Branch']='MS VLSI-CAD'
enroll_29.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_29 = enroll_29.reset_index()
del enroll_29['index']
enroll_29=enroll_29.drop("nan",axis=1)
enroll_29=enroll_29.set_index('NO')


enroll_30=sheet2[467:480]
enroll_30.loc[:,'year'] = 'Aug 2000 to Feb 2002'
enroll_30['Batch']='Batch_3'
enroll_30['Branch']='MS VLSI-CAD'
enroll_30.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_30 = enroll_30.reset_index()
del enroll_30['index']
enroll_30=enroll_30.drop("nan",axis=1)
enroll_30=enroll_30.set_index('NO')


enroll_31=sheet2[481:487]
enroll_31.loc[:,'year'] = 'Feb 2001 to Aug 2002'
enroll_31['Batch']='Batch_4'
enroll_31['Branch']='MS VLSI-CAD'
enroll_31.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_31 = enroll_31.reset_index()
del enroll_31['index']
enroll_31=enroll_31.drop("nan",axis=1)
enroll_31=enroll_31.set_index('NO')


enroll_32=sheet2[488:522]
enroll_32.loc[:,'year'] = 'Aug 2001 to Feb 2003'
enroll_32['Batch']='Batch_5'
enroll_32['Branch']='MS VLSI-CAD'
enroll_32.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_32 = enroll_32.reset_index()
del enroll_32['index']
enroll_32=enroll_32.drop("nan",axis=1)
enroll_32=enroll_32.set_index('NO')


enroll_33=sheet2[523:547]
enroll_33.loc[:,'year'] = 'Feb 2002 to Aug 2003'
enroll_33['Batch']='Batch_6'
enroll_33['Branch']='MS VLSI-CAD'
enroll_33.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_33 = enroll_33.reset_index()
del enroll_33['index']
enroll_33=enroll_33.drop("nan",axis=1)
enroll_33=enroll_33.set_index('NO')


enroll_34=sheet2[548:579]
enroll_34.loc[:,'year'] = 'Aug 2002 to Feb 2004'
enroll_34['Batch']='Batch_7'
enroll_34['Branch']='MS VLSI-CAD'
enroll_34.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_34 = enroll_34.reset_index()
del enroll_34['index']
enroll_34=enroll_34.drop("nan",axis=1)
enroll_34=enroll_34.set_index('NO')


enroll_35=sheet2[580:592]
enroll_35.loc[:,'year'] = 'Feb  2003 to Feb 2005'
enroll_35['Batch']='Batch_8'
enroll_35['Branch']='MS VLSI-CAD'
enroll_35.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_35 = enroll_35.reset_index()
del enroll_35['index']
enroll_35=enroll_35.drop("nan",axis=1)
enroll_35=enroll_35.set_index('NO')


enroll_36=sheet2[593:612]
enroll_36.loc[:,'year'] = 'Aug 2003 to Aug 2005'
enroll_36['Batch']='Batch_9'
enroll_36['Branch']='MS VLSI-CAD'
enroll_36.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_36 = enroll_36.reset_index()
del enroll_36['index']
enroll_36=enroll_36.drop("nan",axis=1)
enroll_36=enroll_36.set_index('NO')


enroll_37=sheet2[613:615]
enroll_37.loc[:,'year'] = ''
enroll_37['Batch']='Batch_10'
enroll_37['Branch']='MS VLSI-CAD'
enroll_37.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_37 = enroll_37.reset_index()
del enroll_37['index']
enroll_37=enroll_37.drop("nan",axis=1)
enroll_37=enroll_37.set_index('NO')


enroll_38=sheet2[616:641]
enroll_38.loc[:,'year'] = 'Aug 2004 to Aug 2006'
enroll_38['Batch']='Batch_11'
enroll_38['Branch']='MS VLSI-CAD'
enroll_38.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_38 = enroll_38.reset_index()
del enroll_38['index']
enroll_38=enroll_38.drop("nan",axis=1)
enroll_38=enroll_38.set_index('NO')


enroll_39=sheet2[642:648]
enroll_39.loc[:,'year'] = 'Aug 2005 Jul 2007'
enroll_39['Batch']='Batch_1'
enroll_39['Branch']='MSc INFORMATION SCIENCE'
enroll_39.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_39 = enroll_39.reset_index()
del enroll_39['index']
enroll_39=enroll_39.drop("nan",axis=1)
enroll_39=enroll_39.set_index('NO')

enroll_40=sheet2[649:676]
enroll_40.loc[:,'year'] = 'Aug 2005 to Aug 2007'
enroll_40['Batch']='Batch_13'
enroll_40['Branch']='MS VLSI-CAD'
enroll_40.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_40 = enroll_40.reset_index()
del enroll_40['index']
enroll_40=enroll_40.drop("nan",axis=1)
enroll_40=enroll_40.set_index('NO')


enroll_41=sheet2[677:684]
enroll_41.loc[:,'year'] = 'Jan 2006 to Dec 2007'
enroll_41['Batch']='Batch_14'
enroll_41['Branch']='MS VLSI-CAD'
enroll_41.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_41 = enroll_41.reset_index()
del enroll_41['index']
enroll_41=enroll_41.drop("nan",axis=1)
enroll_41=enroll_41.set_index('NO')


enroll_42=sheet2[685:716]
enroll_42.loc[:,'year'] = 'Aug 2006 to July 2008'
enroll_42['Batch']='Batch_15'
enroll_42['Branch']='MS VLSI-CAD'
enroll_42.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_42 = enroll_42.reset_index()
del enroll_42['index']
enroll_42=enroll_42.drop("nan",axis=1)
enroll_42=enroll_42.set_index('NO')


enroll_43=sheet2[717:723]
enroll_43.loc[:,'year'] = 'Jan 2007 Dec 2008'
enroll_43['Batch']='Batch_16'
enroll_43['Branch']='MS VLSI-CAD'
enroll_43.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_43 = enroll_43.reset_index()
del enroll_43['index']
enroll_43=enroll_43.drop("nan",axis=1)
enroll_43=enroll_43.set_index('NO')


enroll_44=sheet2[724:764]
enroll_44.loc[:,'year'] = 'Aug 2007Jul 2009'
enroll_44['Batch']='Batch_17'
enroll_44['Branch']='MS VLSI-CAD'
enroll_44.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_44 = enroll_44.reset_index()
del enroll_44['index']
enroll_44=enroll_44.drop("nan",axis=1)
enroll_44=enroll_44.set_index('NO')

enroll_45=sheet2[765:772]
enroll_45.loc[:,'year'] = 'Jan 2008 - Dec 2009'
enroll_45['Batch']='Batch_18'
enroll_45['Branch']='MS VLSI-CAD'
enroll_45.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_45 = enroll_45.reset_index()
del enroll_45['index']
enroll_45=enroll_45.drop("nan",axis=1)
enroll_45=enroll_45.set_index('NO')


enroll_46=sheet2[773:788]
enroll_46.loc[:,'year'] = 'Aug 2008 - July 2010'
enroll_46['Batch']='Batch_19'
enroll_46['Branch']='MS VLSI-CAD'
enroll_46.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_46 = enroll_46.reset_index()
del enroll_46['index']
enroll_46=enroll_46.drop("nan",axis=1)
enroll_46=enroll_46.set_index('NO')


enroll_47=sheet2[789:796]
enroll_47.loc[:,'year'] = 'Jan 2009 to Dec 2010'
enroll_47['Batch']='Batch_20'
enroll_47['Branch']='MS VLSI-CAD'
enroll_47.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_47 = enroll_47.reset_index()
del enroll_47['index']
enroll_47=enroll_47.drop("nan",axis=1)
enroll_47=enroll_47.set_index('NO')
enroll_47=enroll_47.drop("Sl. No.",axis=0)


enroll_48=sheet2[797:837]
enroll_48.loc[:,'year'] = 'Aug 2009 - July 2011'
enroll_48['Batch']='Batch_21'
enroll_48['Branch']='MS VLSI-CAD'
enroll_48.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_48 = enroll_48.reset_index()
del enroll_48['index']
enroll_48=enroll_48.drop("nan",axis=1)
enroll_48=enroll_48.set_index('NO')


enroll_49=sheet2[838:844]
enroll_49.loc[:,'year'] = 'Jan 2010 to Dec 2011'
enroll_49['Batch']='Batch_22'
enroll_49['Branch']='MS VLSI-CAD'
enroll_49.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_49 = enroll_49.reset_index()
del enroll_49['index']
enroll_49=enroll_49.drop("nan",axis=1)
enroll_49=enroll_49.set_index('NO')


enroll_50=sheet2[847:887]
enroll_50.loc[:,'year'] = ' Aug 2010 - July 2012'
enroll_50['Batch']='Batch_23'
enroll_50['Branch']='MS VLSI-CAD'
enroll_50.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_50 = enroll_50.reset_index()
del enroll_50['index']
enroll_50=enroll_50.drop("nan",axis=1)
enroll_50=enroll_50.set_index('NO')


enroll_51=sheet2[891:893]
enroll_51.loc[:,'year'] = 'Jan 2011 to Dec 2012'
enroll_51['Batch']='Batch_24'
enroll_51['Branch']='MS VLSI-CAD'
enroll_51.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_51 = enroll_51.reset_index()
del enroll_51['index']
enroll_51=enroll_51.drop("nan",axis=1)
enroll_51=enroll_51.set_index('NO')


enroll_52=sheet2[896:936]
enroll_52.loc[:,'year'] = 'Aug 2011 - July 2013'
enroll_52['Batch']='Batch_25'
enroll_52['Branch']='MS VLSI-CAD'
enroll_52.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_52 = enroll_52.reset_index()
del enroll_52['index']
enroll_52=enroll_52.drop("nan",axis=1)
enroll_52=enroll_52.set_index('NO')


enroll_75=sheet2[1949:1957]
enroll_75.loc[:,'year'] = 'Aug 2009 to July 2011'
enroll_75['Batch']='Batch_1'
enroll_75['Branch']='MS VLSI-AXIOM'
enroll_75.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_75 = enroll_75.reset_index()
del enroll_75['index']
enroll_75=enroll_75.drop("nan",axis=1)
enroll_75=enroll_75.set_index('NO')


enroll_76=sheet2[1960:1975]
enroll_76.loc[:,'year'] = 'Aug 2010 to July 2012'
enroll_76['Batch']='Batch_2'
enroll_76['Branch']='MS VLSI-AXIOM'
enroll_76.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_76 = enroll_76.reset_index()
del enroll_76['index']
enroll_76=enroll_76.drop("nan",axis=1)
enroll_76=enroll_76.set_index('NO')


enroll_77=sheet2[1978:1989]
enroll_77.loc[:,'year'] = 'Aug 2011 to July 2013'
enroll_77['Batch']='Batch_3'
enroll_77['Branch']='MS VLSI-AXIOM'
enroll_77.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_77 = enroll_77.reset_index()
del enroll_77['index']
enroll_77=enroll_77.drop("nan",axis=1)
enroll_77=enroll_77.set_index('NO')


enroll_78=sheet2[2032:2041]
enroll_78.loc[:,'year'] = 'Aug 2009July 2011'
enroll_78['Batch']='Batch_1'
enroll_78['Branch']='MS DUAL DEGREE'
enroll_78.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_78 = enroll_78.reset_index()
del enroll_78['index']
enroll_78=enroll_78.drop("nan",axis=1)
enroll_78=enroll_78.set_index('NO')


enroll_79=sheet2[2044:2064]
enroll_79.loc[:,'year'] = 'Aug 2010 to July 2012'
enroll_79['Batch']='Batch_2'
enroll_79['Branch']='MS DUAL DEGREE'
enroll_79.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_79 = enroll_79.reset_index()
del enroll_79['index']
enroll_79=enroll_79.drop("nan",axis=1)
enroll_79=enroll_79.set_index('NO')


enroll_80=sheet2[2067:2086]
enroll_80.loc[:,'year'] = 'Aug 2011 to July 2013'
enroll_80['Batch']='Batch_3'
enroll_80['Branch']='MS DUAL DEGREE'
enroll_80.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_80 = enroll_80.reset_index()
del enroll_80['index']
enroll_80=enroll_80.drop("nan",axis=1)
enroll_80=enroll_80.set_index('NO')


enroll_81=sheet2[2108:2123]
enroll_81.loc[:,'year'] = 'Aug 2010 to Jul 2012'
enroll_81['Batch']='Batch_4'
enroll_81['Branch']='MS IT'
enroll_81.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_81 = enroll_81.reset_index()
del enroll_81['index']
enroll_81=enroll_81.drop("nan",axis=1)
enroll_81=enroll_81.set_index('NO')


enroll_82=sheet2[2127:2143]
enroll_82.loc[:,'year'] = 'August2011'
enroll_82['Batch']='Batch_5'
enroll_82['Branch']='MS IT'
enroll_82.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_82 = enroll_82.reset_index()
del enroll_82['index']
enroll_82=enroll_82.drop("nan",axis=1)
enroll_82=enroll_82.set_index('NO')


enroll_83=sheet2[2146:2170]
enroll_83.loc[:,'year'] = 'Aug 2011 to Jul 2013'
enroll_83['Batch']='Batch_1'
enroll_83['Branch']='MS Computing Technologies & Virtualization '
enroll_83.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_83 = enroll_83.reset_index()
del enroll_83['index']
enroll_83=enroll_83.drop("nan",axis=1)
enroll_83=enroll_83.set_index('NO')


enroll_84=sheet2[2173:2182]
enroll_84.loc[:,'year'] = 'Aug 2011 to Jul 2013'
enroll_84['Batch']='Batch_1'
enroll_84['Branch']='MS DUAL - LU & ENU '
enroll_84.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_84 = enroll_84.reset_index()
del enroll_84['index']
enroll_84=enroll_84.drop("nan",axis=1)
enroll_84=enroll_84.set_index('NO')


enroll_39=sheet2[642:648]
enroll_39.loc[:,'year'] = 'Aug 2005 Jul 2007'
enroll_39['Batch']='Batch_1'
enroll_39['Branch']='MSc INFORMATION SCIENCE'
enroll_39.columns = ['NO','ROLL NO','NAME','Gender','State','nan','Year','Batch','Branch']
enroll_39 = enroll_39.reset_index()
del enroll_39['index']
enroll_39=enroll_39.drop("nan",axis=1)
enroll_39=enroll_39.set_index('NO')


# ### convert data frames to csv


def convert_csv(start,end,file_name):
    for i in range(start,end):
        values=(eval(file_name.format(i)))
        values.to_csv(file_name.format(i))
    


convert_csv(1,14,'df{}')

convert_csv(1,105,'enroll_{}')


# ### anonymize roll no. and name


def hash_func(data):
    enroll_select=data.ix[:,0:2]
    s=[]
    for i,val in enroll_select.iterrows() :
        roll=str(val['ROLL NO'])
        name=str(val['NAME'])
        hash_roll = hashlib.md5(roll.encode())
        hash_name = hashlib.md5(name.encode())
        hash_roll = hash_roll.hexdigest()
        hash_name = hash_name.hexdigest()
        s.append([hash_roll,hash_name])
        columns = ['ROLL NO', 'NAME']
        hashed_df=pd.DataFrame(s,columns=columns)
    data_del=data.drop(['ROLL NO','NAME'],axis=1)
    data_del = data_del.reset_index(drop = True)
    hashed_df=pd.concat([hashed_df,data_del],axis=1,join_axes=[hashed_df.index],join='inner')
    hashed_df=hashed_df.set_index([data.index])
    
    return hashed_df

    
    

for g in range(1,106):
    file='enroll_{}'.format(g)
    file=eval(file)
    hashed_file=hash_func(file)
    hashed_file= exec ("hashed_enroll_%s= hashed_file" % (g))


hashed_enroll_1


# ## Visualization


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'Medical Software']
    exec ("file_%s= f" % (i))
    


medical=pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'VLSI Design']
    exec ("file_%s= f" % (i))


vlsi=pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'Embedded Systems']
    exec ("file_%s= f" % (i))


embedded=pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'Embedded & Wireless Technologies']
    exec ("file_%s= f" % (i))


embedded_wireless=pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'Computing Technologies & Virtualization']
    exec ("file_%s= f" % (i))


computing=pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'Information Science']
    exec ("file_%s= f" % (i))


information_science=pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'Embedded & Instrumentation Engg']
    exec ("file_%s= f" % (i))


embedded_instrumentation=pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'Automotive Embedded Systems']
    exec ("file_%s= f" % (i))


automotive=pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'VLSI System Design & Verification']
    exec ("file_%s= f" % (i))


vlsi_sys=pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'Embedded Systems - BE/Btech Grad']
    exec ("file_%s= f" % (i))


embedded_btech = pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'Embedded Systems - BCA/BSc Grad']
    exec ("file_%s= f" % (i))


embedded_bca = pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'IT Management']
    exec ("file_%s= f" % (i))


it_management = pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')
it_management


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'MSc DDES (Jan - July)']
    exec ("file_%s= f" % (i))


Msc_ddes = pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')
Msc_ddes


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'MSc Info. Science (Jan - July)']
    exec ("file_%s= f" % (i))


Msc_info_sc = pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')
Msc_info_sc


s=[]
for i in range(1,14):
    f='df{}'.format(i)
    f= eval(f)
    f=f.loc[f['Branches'] == 'VLSI CAD']
    exec ("file_%s= f" % (i))


vlsi_cad = pd.concat([file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9,file_10,file_11,file_12,file_13],axis=0,join='inner')


vlsi_cad = vlsi_cad.reset_index(drop=True)
vlsi_cad

from nvd3 import multiBarChart
import nvd3
nvd3.ipynb.initialize_javascript()

from IPython.core.display import display, HTML

chart = multiBarChart(width=1200, height=500, x_axis_format=None)
#xdata = list(vlsi_cad['year_intake'])
xdata = ['VLSI_CAD2011', 'VLSI_CAD2010', 'VLSI_CDA2009', 'VLSI_CAD2008', 'VLSI_CAD2007', 'VLSI_CAD2006', 'VLSI_CAD2005', 'VLSI_CAD2004', 'VLSI_CAD2003']
#ydata1 = list(vlsi_cad['Class Strength'])
ydata1 = [43, 46, 46, 23, 45, 36, 33, 27, 29]
#ydata2 = list(vlsi_cad['# of placed students'])
ydata2 = [39, 41, 34, 12, 23, 29, 23, 22, 20]

chart.add_serie(name="class strength", y=ydata1, x=xdata)
chart.add_serie(name="placed students", y=ydata2, x=xdata)
chart.buildhtml()
display(HTML(chart.htmlcontent))



list(df1['Branches'])
list(df1['Total placement %'])


from nvd3 import pieChart
chart = pieChart(name='pieChart', color_category='category20c',
                 height=700, width=700)

xdata = ['Medical Software',
 'VLSI Design',
 'Embedded Systems',
 'Embedded & Wireless Technologies',
 'Computing Technologies & Virtualization',
 'Information Science',
 'Embedded & Instrumentation Engg',
 'Automotive Embedded Systems',
 'All branch without ESIGELEC',
 'All branches']
ydata = [75,63.15,77.5510204081633,77.7777777777778,80,100,100,100,73.5537190082645,77.7777777777778]

extra_serie = {"tooltip": {"y_start": "", "y_end": " per"}}
chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
chart.buildhtml()
display(HTML(chart.htmlcontent))


ydata2


import matplotlib.pyplot as plt
 
# Data to plot
labels = 'Medical Software','VLSI Design','Embedded Systems','Embedded & Wireless Technologies','Computing Technologies & Virtualization','Information Science','Embedded & Instrumentation Engg','Automotive Embedded Systems','All branch without ESIGELEC','All branches'
sizes = [75,63.15,77.5510204081633,77.7777777777778,80,100,100,100,73.5537190082645,77.7777777777778]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink','darkblue','white','yellow','red','lightgreen']
#explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
