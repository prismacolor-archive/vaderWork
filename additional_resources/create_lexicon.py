import csv
import re
import statistics

complete_lexicon = open('../vaderSentiment/paycor_mod_lexicon.txt', 'a')

# any time we make an update we will want to only include the new words so we don't have duplicates
# make sure in upcoming edits to start the loop at the row where new words have been added
with open('../Paycor_Vader_docs/lexicon_scored.csv') as lexicon_file:
    file_reader = csv.reader(lexicon_file, delimiter=',')
    line_count = 0

    # loop through the lines in the original paycor lexicon csv
    for row in file_reader:
        if line_count == 0:
            # ignore the column headers, can edit to be if line_count > ?, continue, to skip previous words
            line_count += 1
            continue
        else:
            # everything comes in as strings but for the final txt file we need some formatting to match final output
            # format the mean as a one digit float
            mean_score = float(format(float(row[-1]), '.1f'))

            # format the scores as numbers to get the standard dev score
            numbers = ['-4', '-3', '-2', '-1', '0', '1', '2', '3', '4']
            strip_scores = row[-2].replace('[', '').replace(']', '').replace(',', '')
            clean_scores = [int(i) for i in strip_scores.split() if i in numbers]

            # format standard dev as a five digit float
            stan_dev = float(format(statistics.stdev(clean_scores), '.5f'))

            # store the results in a new variable list
            new_row = [row[1] + '\t' + str(mean_score) + '\t' + str(stan_dev) + '\t' + row[-2]]
            new_row = (' '.join(new_row))

            # write it to a new txt file
            complete_lexicon.write('\n' + new_row)

            line_count += 1


lexicon_file.close()
complete_lexicon.close()
