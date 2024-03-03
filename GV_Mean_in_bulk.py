from GV_Mean_lib import get_mean_gv_percentage

files_to_analyse = [ 
    {
        'file_name': '~/Downloads/MembraneExperiments_CTR shScramble Exp1.xlsx', 
        'sheet_name': 'C2Rednew_CTR (2)'
    },
    {
        'file_name': 'xxx', 
        'sheet_name': 'yyy'
    }, 
    {
        'file_name': 'xxx', 
        'sheet_name': 'yyy'
    }, 
]

if __name__ == '__main__':
    for current_file in files_to_analyse:
        print('-----------------\n')
        file_name = current_file['file_name']
        sheet_name = current_file['sheet_name']
        print(f'The file "{file_name}" is now beginning to be processed.\n')
        try:
            get_mean_gv_percentage(file_name, sheet_name, verbose = True)
        except FileNotFoundError:
            print(f'The file "{file_name}" could not be found. Please verify the file path and ensure it exists in the specified location.')
        print('')
     
