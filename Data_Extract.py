import json
import csv

SNR_CSV = open('./SNR.csv')
SNR_data = csv.reader(SNR_CSV, delimiter=',')

file = open('./summary.json')
data = json.load(file)

one_percentile = data['active_sensor_stats']['one_percentile']

aligned_count = data['active_sensor_stats']['one_percentile']['aligned_count']
total_pc_count = one_percentile['total_pc_count']
cumsum_tot_error_pct_80at75 = data['heatmaps']['80%_@_75']['cumsum_tot_error_pct']['-1']
depth80at75 = data['heatmaps']['80%_@_75']['depth']['-1'][0]
# aligned_32hps = data['heatmaps']['80%_@_75']['depth']['-1'][1] # Column L
bp50greater_than985_32hps = data['n_sensors_above_target_accuracy']['98.5']['50']
bp75greater_than985_32hps = data['n_sensors_above_target_accuracy']['98.5']['75']
n_sensors_act = data['n_sensors_act']
# n_sensors_aligned = data['n_sensors_aligned'] # Column L

# CLuster size up to 15 sensors
cs = data['cluster_size']
cluster_list = [cs[str(x)] for x in range(1,16)]
surface_hit = sum(cluster_list)

# ------------------- SNR data comes from SNR.csv -----------------------
first_line = next(SNR_data)

snr_csv_list = list(SNR_data)
jumps_50 = 10
jumps_std = 13
jumps_raw_50 = 4

# Key: AVG(K26, K28, K30, K32, K34)
key_list = [
    abs(float(snr_csv_list[24][jumps_50])),
    abs(float(snr_csv_list[26][jumps_50])),
    abs(float(snr_csv_list[28][jumps_50])),
    abs(float(snr_csv_list[30][jumps_50])),
    abs(float(snr_csv_list[32][jumps_50]))
]

# Noise: AVG(N24, N36, N43, N77, N113, N115, N149, N185, N192, N226, N262, N264, N298, N334, N341, N375, N411, N413, N447, N483, N490, N524, N560, N562, N596, N632)
noise_list = [
    abs(float(snr_csv_list[22][jumps_std])),
    abs(float(snr_csv_list[34][jumps_std])),
    abs(float(snr_csv_list[41][jumps_std])),
    abs(float(snr_csv_list[75][jumps_std])),
    abs(float(snr_csv_list[111][jumps_std])),
    abs(float(snr_csv_list[113][jumps_std])),
    abs(float(snr_csv_list[147][jumps_std])),
    abs(float(snr_csv_list[183][jumps_std])),
    abs(float(snr_csv_list[190][jumps_std])),
    abs(float(snr_csv_list[224][jumps_std])),
    abs(float(snr_csv_list[260][jumps_std])),
    abs(float(snr_csv_list[262][jumps_std])),
    abs(float(snr_csv_list[296][jumps_std])),
    abs(float(snr_csv_list[332][jumps_std])),
    abs(float(snr_csv_list[339][jumps_std])),
    abs(float(snr_csv_list[373][jumps_std])),
    abs(float(snr_csv_list[409][jumps_std])),
    abs(float(snr_csv_list[411][jumps_std])),
    abs(float(snr_csv_list[445][jumps_std])),
    abs(float(snr_csv_list[481][jumps_std])),
    abs(float(snr_csv_list[488][jumps_std])),
    abs(float(snr_csv_list[522][jumps_std])),
    abs(float(snr_csv_list[558][jumps_std])),
    abs(float(snr_csv_list[560][jumps_std])),
    abs(float(snr_csv_list[594][jumps_std])),
    abs(float(snr_csv_list[630][jumps_std]))
]

jump_warmup_list= [
    (float(snr_csv_list[5][jumps_raw_50])),
    (float(snr_csv_list[7][jumps_raw_50])),
    (float(snr_csv_list[9][jumps_raw_50])),
    (float(snr_csv_list[11][jumps_raw_50])),
    (float(snr_csv_list[13][jumps_raw_50])),
    (float(snr_csv_list[15][jumps_raw_50]))
    ]
jump_b_list= [
    (float(snr_csv_list[22][jumps_raw_50])),
    (float(snr_csv_list[34][jumps_raw_50])),
    (float(snr_csv_list[41][jumps_raw_50])),
    (float(snr_csv_list[75][jumps_raw_50])),
    (float(snr_csv_list[111][jumps_raw_50])),
    (float(snr_csv_list[113][jumps_raw_50])),
    (float(snr_csv_list[147][jumps_raw_50])),
    (float(snr_csv_list[183][jumps_raw_50])),
    (float(snr_csv_list[190][jumps_raw_50])),
    (float(snr_csv_list[224][jumps_raw_50])),
    (float(snr_csv_list[260][jumps_raw_50])),
    (float(snr_csv_list[262][jumps_raw_50])),
    (float(snr_csv_list[296][jumps_raw_50])),
    (float(snr_csv_list[332][jumps_raw_50])),
    (float(snr_csv_list[339][jumps_raw_50])),
    (float(snr_csv_list[373][jumps_raw_50])),
    (float(snr_csv_list[409][jumps_raw_50])),
    (float(snr_csv_list[411][jumps_raw_50])),
    (float(snr_csv_list[445][jumps_raw_50])),
    (float(snr_csv_list[481][jumps_raw_50])),
    (float(snr_csv_list[488][jumps_raw_50])),
    (float(snr_csv_list[522][jumps_raw_50])),
    (float(snr_csv_list[558][jumps_raw_50])),
    (float(snr_csv_list[560][jumps_raw_50])),
    (float(snr_csv_list[594][jumps_raw_50])),
    (float(snr_csv_list[630][jumps_raw_50]))
]

key = round(sum(key_list) / len(key_list), 1)
noise = round((sum(noise_list) / len(noise_list)), 1)
jump_warmup = round((sum(jump_warmup_list) / len(jump_warmup_list)), 1)
jump_b = round((sum(jump_b_list) / len(jump_b_list)), 1)


fieldnames = ['Acc80@75', 'Depth80@75','Key', 'Noise', 'Active','Aligned 32 HPs', 'BP50>98.5 32HPs', 'BP75>98.5 32HPs', 'Polyclonal (PC)','Surface Hit','Jump Warm Up','Jump B Flows']

data_for_spreadsheet = {
    "Acc80@75": 1 - cumsum_tot_error_pct_80at75 / 100,
    "Depth80@75": depth80at75,
    "Key": key,
    "Noise": noise,
    "Active": 5 * n_sensors_act,
    "Aligned 32 HPs": aligned_count,
    "BP50>98.5 32HPs": bp50greater_than985_32hps,
    "BP75>98.5 32HPs": bp75greater_than985_32hps,
    "Polyclonal (PC)": total_pc_count,
    "Surface Hit": surface_hit,
    "Jump Warm Up":jump_warmup,
    "Jump B Flows":jump_b
}
with open('seq_stats.csv', mode='w') as file:
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow(data_for_spreadsheet)

print('Learning how to make pull request on Github')

print(' ----------------- Successfully extracted relevant sequencing data to seq_stats.csv! -----------------')
