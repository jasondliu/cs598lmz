import codecs
codecs.register_error("strict", codecs.ignore_errors)
import csv

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("USAGE: python evaluator.py [FILE]")
        exit(1)

    # 引数から入力ファイルパスを取得
    input_path = sys.argv[1]

    # 入力ファイル(CSV形式)の準備
    input_file = codecs.open(input_path, "r", "utf_8", "ignore")
    reader = csv.reader(input_file)

    # 結果出力の準備
    output_file = codecs.open("result.csv", "a", "utf_8", "ignore")
    writer = csv.writer(output_file, lineterminator='\n')

    # チーム名ファイルの準備
    team_names_path = os.path
