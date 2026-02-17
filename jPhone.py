# jPhone Ver14

# 共通
import random
names = []
address = {}
point = 0
line = '--------------------'
loop_flg = True

# 電卓
def calc_main():
    """
    計算機能
    計算に必要な機能を入力させ、calcを呼び出し、計算結果を表示する.
    """
    print('【電卓】')
    calc()

def calc():
    """計算処理
    
    引数で渡された値を演算子にしたがって計算し
    結果を返す.
    
        引数：
            val(int):計算対象の値.
            val2(int):計算対象の値.
            op(str):演算子.
        戻り値：
            goukei:計算結果.
    """
    val2 = 0
    val = int(input('数値1＞'))
    en = input('演算子＞')
    if en != 'bin':
        val2 = int(input('数値2＞'))
    if en == '+' :
        goukei = val + val2
    elif en == '-':
        goukei = val - val2
    elif en == '*':
        goukei = val * val2
    elif en == '/':
        goukei = val / val2
    elif en == '**':
        goukei = val ** val2
    elif en == 'bin':
        nisin = []
        rrr = ['']
        while val > 1:
            val2 = int(val % 2)
            if val2 > 0:
                nisin.append('1')
            else:
                nisin.append('0')
            val = val / 2
        if val < 2:
            if val == 1:
                nisin.append('1')
            elif val == 0:
                nisin.append('0')
        i = len(nisin)-1
        while i >= 0:
            rrr[0] = rrr[0] + nisin[i]
            i = i - 1
        goukei = rrr
    else:
        goukei = 'ERROR'
    print(line)
    print(goukei)
    print(line)
    

# 連絡先
def address_main():
    """
    連絡先機能
    　連絡先機能のメニューを入力させ、入力された番号に従って
    処理を振り分ける.「99,戻る」が押されるまで連絡の処理を繰り返す.
    """
    print('【連絡先】')
    address_sub_menu_item = '２１．新規連絡先\t２２．連絡先一覧'
    address_sub_menu_item2 = '２３．ソート（昇順）\t２４．連絡先削除'
    address_sub_menu_item3 = '２５．連絡先検索\t９９．戻る'
    print(address_sub_menu_item)
    print(address_sub_menu_item2)
    print(address_sub_menu_item3)
    address_sub_menu = int(input('メニュー選択＞'))
    print()
    if address_sub_menu == 21:
        address_append()
    elif address_sub_menu == 22:
        address_list()
    elif address_sub_menu == 23:
        address_sort()
    elif address_sub_menu == 24:
        address_remove()
    elif address_sub_menu == 25:
        address_search()
    elif address_sub_menu == 99:
        main()
    else:
        print('メニューは、'+ address_sub_menu_item.replace('\t', '').replace('\n', '') + address_sub_menu_item2.replace('\t', '').replace('\n', '') + address_sub_menu_item3.replace('\t', '').replace('\n', '') + 'を選択してください。')
        address_main()

def address_append():
    """連絡先の追加
    　氏名と電話番号を入力させ、連絡先情報として管理する.
    """
    global names
    global address
    print('【新規連絡先】')
    print('1件目')
    print(line)
    sei = input('姓(カナ)　＞')
    mei = input('名(カナ)　＞')
    denwa = input('電話番号　＞')
    name = (sei + mei)
    names.append(name)
    address[name] =  (denwa)
    print()
    print('2件目')
    print(line)
    sei2 = input('姓(カナ)　＞')
    mei2 = input('名(カナ)　＞')
    denwa2 = input('電話番号　＞')
    name2 = (sei2 + mei2)
    names.append(name2)
    address[name2] =  (denwa2)
    print()
    print('3件目')
    print(line)
    sei3 = input('姓(カナ)　＞')
    mei3 = input('名(カナ)　＞')
    denwa3 = input('電話番号　＞')
    name3 = (sei3 + mei3)
    names.append(name3)
    address[name3] =  (denwa3)
    print()
    print(names)
    print(address)
    address_main()

def address_list():
    print('【連絡先一覧】')
    for index, val in enumerate(names):
        print(index,val)
    no = int(input('Noを入力＞'))
    while index != -1:
        if no == index:
            print(names[index]+'さんの電話番号：'+address[names[index]])
            address_main()
        else:
            index = index-1
    if index == -1:
        print('範囲外のNoが入力されました。')

def address_sort():
    i = 0
    sw = 0
    k = 1
    j = len(names)-1
    while sw != 1:
        if k <= j:
            fmt = '{}回目'.format(k)
            print(fmt)
            if k == 1:
                print(names)
            while i < j:
                if names[i] >= names[i+1]:
                    sort = []
                    sort.append(names[i+1])
                    sort.append(names[i])
                    names[i+1] = sort[-1]
                    names[i] = sort[-2]
                    print(names)
                i = i + 1
            print()
            address_main()
        else:
            sw = 1
        i = 0
        k = k + 1

def address_remove():
    print('【連絡先削除】')
    for index, val in enumerate(names):
        print(index,val)
    no = int(input('Noを入力＞'))
    while index != -1:
        if no == index:
            d = input(names[index]+'さんの情報を削除してもよいですか？(yes/no)＞：')
            if d == 'yes':
                print('削除しました。')
                del(address[names[index]])
                del(names[index])
                address_main()
            else:
                print('削除を取り消しました。')
                address_main()
        else:
            index = index-1
    if index == -1:
        print('範囲外のNoが入力されました。')

def address_search():
    print('【連絡先検索】')
    n = 0
    na = input('氏名を入力＞')
    while na != names[n]:
        if n == len(names)-1:
            print(na+'は見つかりませんでした。')
            address_main()
        else:
            n = n+1
    if na == names[n]:
        fmt = '{}さんの電話番号：{}'.format(na,address[names[n]])
        print(fmt)
        address_main()

# ゲーム
def game_main():
    """
    ゲーム機能
    """
    global point
    print('【ゲーム】')
    game_submenu_item = '３１．ポイント照会\t３２．じゃんけん\t９９．戻る'
    print(game_submenu_item)
    game_submenu = int(input('メニュー選択＞'))
    if game_submenu == 31:
        point_disp()
    elif game_submenu == 32:
        jyanken_main()
    elif game_submenu == 99:
        main()
    else:
        print('メニューは、'+ game_submenu_item.replace('\t', '').replace('\n', '') + 'を選択してください。')

def point_disp():
    global point
    print('【ポイント照会】')
    fmt = '現在、{}ポイントです。'.format(point)
    print(fmt)
    game_main()

def jyanken_main():
    print('【じゃんけん】')
    print('じゃーんけーん・・・')
    try:
        te = {0:'グー',1:'チョキ',2:'パー'}
        you = int(input('0:グー/1:チョキ/2:パー＞'))
        if te[you] == 'グー' or 'チョキ' or 'パー':
            com = random.randint(0,2)
            fmt = 'COM：{}'.format(te[com])
            print('ぽん！！！')
            print(fmt)
            fmt = 'あなた：{}'.format(te[you])
            print(fmt)
            jyanken_judge(you,com)
    except ValueError:
        print('入力に誤りがあります。',te,'を入力してください。')
    except KeyError:
        print('入力に誤りがあります。',te,'を入力してください。')


def jyanken_judge(you,com):
    """じゃんけんの判定
    　引数で渡されたユーザーの手とCOMの手を
    もとに、じゃんけんの勝敗を判定する.判定条
    件に一致しない場合（ユーザーの手が範囲外の場
    合など）、エラーメッセージを表示する。
    　引数：
        you(int):ユーザーの手(0:グー/1:チョキ/2:パー).
        com(int):COMの手(0:グー/1:チョキ/2:パー).
    　戻り値：
        result:勝敗の結果
    （WIN/DROW/LOSE).
    """
    if (you==0 and com==1) or (you==1 and com==2) or (you==2 and com==0):
        print(line)
        print('勝ち！')
        print(line)
        result = 'WIN'
    elif (you==1 and com==0) or (you==2 and com==1) or (you==0 and com==2):
        print(line)
        print('負け')
        print(line)
        result = 'LOSE'
    else:
        print(line)
        print('あいこ')
        print(line)
        result = 'DROW'
    return point_update(result)

def point_update(result):
    """ポイント更新
    　勝敗に応じてポイントを更新する.今回獲
    得したポイント数を表示する.
    　引数：
    　result:勝敗の結果（WIN/DROW/LOSE）.
    """
    global point
    if result == 'WIN':
        point+=10
        print('10ポイント獲得。')
    elif result == 'DROW':
        point+=5
        print('5ポイント獲得。')
    game_main()

# メイン
def main():
    global loop_flg
    while loop_flg:
        print('【ホーム画面】')
        home_menu_item = '１．電卓\t\t２．連絡先'
        home_menu_item2 = '３.ゲーム'
        print(home_menu_item)
        print(home_menu_item2)
        print('９９．終了')
        menu = int(input('メニュー選択＞'))
        print()
        if menu == 1:
            calc_main()
        elif menu == 2:
            address_main()
        elif menu == 3:
            game_main()
        elif menu == 99:
            print(line)
            print('【終了】')
            print(line)
            loop_flg = False

# 実行制御
title = 'jPhone Ver13'
print(line)
print(title)
print(line)
if __name__ == '__main__':
    main()