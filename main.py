# json整形
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

# 自作モジュール
import sendmail
import getrequests


result = getrequests.get_requests("魔女と百騎兵") # 1件もヒットしない検索キーワードを入力
formatted_data = getrequests.shape_json(result) # jsonを整形
sendmail = sendmail.sendmail()

if result["resultCount"] != 0: # もし1件でもヒットしたら通知する
    # sendmail.sendmail()
    print("\n" + highlight(formatted_data, JsonLexer(), TerminalFormatter()))
    print("\033[32m" + str(len(result["results"])) + " search results were " + "found!" + "\033[32m" + "\n")
else:
    print("\n" + highlight(formatted_data, JsonLexer(), TerminalFormatter()))
    print("\033[36m" + "No search results were found." + "\033[0m" + "\n")
