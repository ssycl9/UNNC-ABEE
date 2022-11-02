import pandas as pd
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

def eplus_to_datetime(date_str):
	if date_str[-8:-6] != '24':
		dt_obj = pd.to_datetime(date_str)
	else: 
		date_str = date_str[0: -8] + '00' + date_str[-6:]
		dt_obj = pd.to_datetime(date_str) + dt.timedelta(days=1)
	return dt_obj

def plot_1D_result(output_paths,plot_column_name,y_axis_title,
                    plot_title,output_dir):
    fontsize = 20
    fig, axs = plt.subplots(1, 1, figsize=(20,10))

    for parameter_value in output_paths.key():

        this_path = output_paths[parameter_value]

        this_df = pd.read_csv(this_path)

        this_df['Date/Time'] = '2002' + this_df['Date/Time']
        this_df['Date/Time'] = this_df['Date/Time'].apply(eplus_to_datetime)

        data_st_date = this_df.iloc[0]['Date/Time']
        data_ed_date = this_df.iloc[-1]['Date/Time']

        date_list = this_df['Date/Time']

        this_y = this_df[plot_column_name].values

        axs.plot(date_list, this_y, label = parameter_value)
    
    datetime_ax_loc = mdates.HourLocator()  
    datetime_ax_fmt = mdates.DateFormatter('%H:%M')
    axs.xaxis.set_major_locator(datetime_ax_loc)
    axs.xaxis.set_major_formatter(datetime_ax_fmt)
    for tick in axs.xaxis.get_major_ticks():
        tick.label.set_fontsize(fontsize*0.8) 
    for tick in axs.yaxis.get_major_ticks():
        tick.label.set_fontsize(fontsize*0.8)
    axs.tick_params('x', labelrotation=45)
    axs.set_xlabel('Time (%s to %s)'%(data_st_date, data_ed_date),
                  fontsize = fontsize)
    axs.set_ylabel('Air Temperature (C)',
                  fontsize = fontsize)
    axs.legend(fontsize = fontsize)

    plt.title(plot_title,fontsize = fontsize)

    fontsize_path = output_dir + '/plot_figure.pdf'
    plt.savefig(fontsize_path)

    return None
