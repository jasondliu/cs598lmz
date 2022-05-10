import sys, threading

def run():
	match_path = sys.argv[1]
	lib_path = sys.argv[2]
	output_path = sys.argv[3]
	total_match_num = int(sys.stdin.readline())
	for line in sys.stdin:
		if line.strip() == 'done':
			break
		parts = line.strip().split()
		match_id = int(parts[0])
		match_round = parts[1]
		match_time = int(parts[2])
		match_team1 = parts[3]
		match_team2 = parts[4]
		match_result = int(parts[5])
		match_score = [int(x) for x in parts[6].split(duel_config.score_sub_field_separator)]
		match_filename = output_path+'/'+str(match_id)

		cmd = duel_config.match_generate_cmd.format(
			lib_path=lib_path,
	
