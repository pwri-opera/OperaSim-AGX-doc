#!/usr/bin/env python
# coding: UTF-8
import rospy
import time
import sys
import os
from hello.msg import *

def func_param_read(str):
    rospy.loginfo("move_param_data_01.txt")
    with open("/home/numata_pw/catkin_ws/src/hello/src/move_param_data_01.txt", "r") as f:
        while True:
        # ファイルの先頭から一行ずつ読み込む
            line = f.readline()
            char_posf = line.find(",") 
            char_len = len(line)
            char_posb = -(len(line)-char_posf-1)
            char_f = line[:char_posf]
            char_b = line[char_posb:]
           
        # 変数が一致したらループを抜ける
            if str == char_f:
                 break

    rospy.loginfo(char_b)
    return char_b

# メイン
def main():
    # パブリッシャーの生成
    pub = rospy.Publisher("zx120/boom/cmd", MyString, queue_size=10)
    # ノードの初期化
    rospy.init_node("hello", anonymous=True)
    rospy.loginfo("boom=%s", len(sys.argv))

    if len(sys.argv) == 2:
       str = float(sys.argv[1])
    else:
       str = float(func_param_read("zx120_BOOM"))
    
    if (str < -1.22) or (str > 0.767):
        rospy.loginfo("parameter error !!")
        exit()
    else:
        rospy.loginfo("boom:%s", str)

    while not rospy.is_shutdown():

        # メッセージの生成
        msg = MyString()
        msg.data = str
     
        # ログ出力
        rospy.loginfo("boom_msg=%s", msg)
 
        # メッセージの送信
        pub.publish(msg)
        exit()

if __name__ == "__main__":
    main()

