import pandas as pd 

# 4
def correctDateFormat(df):
	# move data from columns to rows
	# create two new columns for date and confirmed
	# add new row for each date x state
	df = df.melt(id_vars=df.columns[0:4], var_name="Date", value_name="Confirmed")

	# convert date to datetime 
	df["Date"] = pd.to_datetime(df["Date"])
	return df

	# use to group data for a country 
	# pass function your df and country's name as a string
def aggregateCountry(df, country):
	data = df.loc[df["Country/Region"] == country]
	return data.groupby("Date", as_index=False).sum()

# 15
def topCorrelation(df, topColumn, n):
	corrs = []
	countries = pd.uniqe(df["Country/Region"])

	empty = pd.DataFrame()
	repeat = []
	for country1 in countries:
		for country2 in countries:
			if country1 != country2:

				x = empty.copy()
				y = empty.copy()
				z = empty.copy()

				x = df.loc[df["Country/Region"] == country1]
				y = df.loc[df["Country/Region"] == country2]

				z = pd.merge(x, y, on="Date")

				print(z[str(tColumn) + " _x "].corr(z[str(tColumn)+ "_y "]))



				










	
