ROSと連携時の送受信データ
=========================

.. note::

   本ページの内容は、OperaSim-AGX リポジトリの ``main`` ブランチの状態を前提としています。
   各トピック名・メッセージ型は、将来の更新により変更される可能性があります。

OperaSim-AGX では、`ROS-TCP-Connector <https://github.com/Unity-Technologies/ROS-TCP-Connector>`_
を介して ROS (ROS 1 / ROS 2) と通信します。

建設機械とのコマンド・状態量のやり取りには、`com3_ros <https://github.com/pwri-opera/com3_ros>`_ (=OPERAにおける共通制御信号)で定義されている
独自のメッセージ型を利用しています。実装は Unity プロジェクト内の
``Assets/RosMessages/msg`` 以下のソースコードを参照してください。

.. note::

   以下の表に出てくる「車体名」は、
   Unity シーン上の建設機械モデルのルート GameObject 名に対応します
   (例: ``zx120``, ``ic120`` など)。


油圧ショベル
------------

ROS → Unity (建機へのコマンド)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 油圧ショベル: ROS → Unity (コマンド)
   :header-rows: 1
   :widths: 30 30 20 20

   * - 項目
     - トピック名
     - メッセージ型
     - 備考
   * - フロント (ブーム, アーム, バケット, 旋回) 動作指令
     - ``/車体名/front_cmd``
     - ``com3_ros/msg/JointCmd``
     - 以下の順に指令値を格納::

         0: bucket_joint
         1: arm_joint
         2: boom_joint
         3: swing_joint
   * - 左右クローラへの動作指令
     - ``/車体名/track_cmd``
     - ``com3_ros/msg/JointCmd``
     - 以下の順に指令値を格納::

         0: left_track
         1: right_track
   * - 車両中心の並進移動速度/回転速度指令
     - ``/車体名/cmd_vel``
     - ``geometry_msg/msg/Twist``
     - 並進速度・角速度指令
   * - 非常停止
     - ``/車体名/emg_stop_cmd``
     - ``std_msgs/msg/Bool``
     - ``true``: その場で停止


Unity → ROS (建機の情報)
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 油圧ショベル: Unity → ROS (情報)
   :header-rows: 1
   :widths: 30 30 20 20

   * - 項目
     - トピック名
     - メッセージ型
     - 備考
   * - 各関節の角度, 角速度
     - ``/車体名/joint_states``
     - ``sensor_msgs/msg/JointState``
     - 以下の順で情報が格納される::

         0: bucket_joint
         1: arm_joint
         2: boom_joint
         3: swing_joint
         4: right_track_joint
         5: left_track_joint
   * - ローカル座標系における車両の中心姿勢
     - ``/車体名/odom_pose``
     - ``nav_msgs/msg/Odometry``
     - シミュレータ内ローカル座標系での位置・姿勢
   * - グローバル(平面直角)座標系における車両の中心姿勢
     - ``/車体名/global_pose``
     - ``nav_msgs/msg/Odometry``
     - 地理座標系と対応づけたグローバル座標
   * - 油圧アクチュエータのメイン圧力
     - ``/車体名/main_fluid_pressure``
     - ``com3_ros/sensor_msgs/FluidPressure``
     - 以下の順で情報が格納される::

         0:  boom_up_main_pressure
         1:  boom_down_main_pressure
         2:  arm_crowd_main_pressure
         3:  arm_dump_main_pressure
         4:  bucket_crowd_main_pressure
         5:  bucket_dump_main_pressure
         6:  swing_right_main_pressure
         7:  swing_left_main_pressure
         8:  right_track_forward_main_prs
         9:  right_track_backward_main_prs
         10: left_track_forward_main_prs
         11: left_track_backward_main_prs
         12: attachment_a_main_pressure
         13: attachment_b_main_pressure
         14: assist_a_main_pressure
         15: assist_b_main_pressure
   * - 油圧アクチュエータのパイロット圧力
     - ``/車体名/main_fluid_pressure``
     - ``com3_ros/sensor_msgs/FluidPressure``
     - 以下の順で情報が格納される::

         0:  boom_up_pilot_pressure
         1:  boom_down_pilot_pressure
         2:  arm_crowd_pilot_pressure
         3:  arm_dump_pilot_pressure
         4:  bucket_crowd_pilot_pressure
         5:  bucket_dump_pilot_pressure
         6:  swing_right_pilot_pressure
         7:  swing_left_pilot_pressure
         8:  right_track_forward_pilot_prs
         9:  right_track_backward_pilot_prs
         10: left_track_forward_pilot_prs
         11: left_track_backward_pilot_prs
         12: attachment_a_pilot_pressure
         13: attachment_b_pilot_pressure
         14: assist_a_pilot_pressure
         15: assist_b_pilot_pressure
   * - 上部構造体の旋回角度
     - ``/車体名/upper_body_rot``
     - ``sensor_msgs/msg/Imu``
     - IMU 形式で上部旋回角を出力
   * - バケット内土量
     - ``/車体名/soil_volume``
     - ``std_msg/msg/Float64``
     - 推定土量


クローラダンプ
--------------

ROS → Unity (建機へのコマンド)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: クローラダンプ: ROS → Unity (コマンド)
   :header-rows: 1
   :widths: 30 30 20 20

   * - 項目
     - トピック名
     - メッセージ型
     - 備考
   * - 旋回, ダンプの動作指令
     - ``/車体名/rot_dump_cmd``
     - ``com3_ros/msg/JointCmd``
     - 以下の順で指令値を格納::

         0: rotate_joint
         1: dump_joint
   * - 左右クローラへの動作指令
     - ``/車体名/track_cmd``
     - ``com3_ros/msg/JointCmd``
     - 以下の順で指令値を格納::

         0: right_track
         1: left_track
   * - 走行ボリュームの動作指令
     - ``/車体名/track_volume_cmd``
     - ``com3_ros/msg/JointCmd``
     - 以下の順で指令値を格納::

         0: forward_volume
         1: turn_volume

       それぞれの effort に ``-1.0 ~ 1.0`` の値を設定する。
   * - 車両中心の並進移動速度/回転速度指令
     - ``/車体名/cmd_vel``
     - ``geometry_msg/msg/Twist``
     - 並進速度・角速度指令
   * - 非常停止
     - ``/車体名/emg_stop_cmd``
     - ``std_msgs/msg/Bool``
     - ``true``: その場で停止


Unity → ROS (建機の情報)
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: クローラダンプ: Unity → ROS (情報)
   :header-rows: 1
   :widths: 30 30 20 20

   * - 項目
     - トピック名
     - メッセージ型
     - 備考
   * - 各関節の角度, 角速度
     - ``/車体名/joint_state``
     - ``sensor_msgs/msg/JointState``
     - 以下の順で情報が格納される::

         0: rotate_joint
         1: dump_joint
         2: right_track_joint
         3: left_track_joint
   * - ローカル座標系における車両の中心姿勢
     - ``/車体名/odom_pose``
     - ``nav_msgs/msg/Odometry``
     - -
   * - グローバル(平面直角)座標系における車両の中心姿勢
     - ``/車体名/global_pose``
     - ``nav_msgs/msg/Odometry``
     - 
   * - 油圧アクチュエータのメイン圧力
     - ``/車体名/main_fluid_pressure``
     - ``com3_ros/sensor_msgs/FluidPressure``
     - - TBD
   * - 油圧アクチュエータのパイロット圧力
     - ``/車体名/main_fluid_pressure``
     - ``com3_ros/sensor_msgs/FluidPressure``
     - - TBD
   * - 上部構造体の旋回角度
     - ``/車体名/upper_body_rot``
     - ``sensor_msggs/msg/Imu``
     - -
   * - バケット内土量
     - ``/車体名/soil_volume``
     - ``std_msg/msg/Float64``
     - -


ブルドーザ
----------

ROS → Unity (建機へのコマンド)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: ブルドーザ: ROS → Unity (コマンド)
   :header-rows: 1
   :widths: 30 30 20 20

   * - 項目
     - トピック名
     - メッセージ型
     - 備考
   * - ブレード (リフト, チルト, アングル) 動作指令
     - ``/車体名/blade_cmd``
     - ``com3_ros/msg/JointCmd``
     - 配列に以下の順に指令値を格納::

         0: lift_joint
         1: tilt_joint
         2: angle_joint
   * - 左右クローラへの動作指令
     - ``/車体名/track_cmd``
     - ``com3_ros/msg/JointCmd``
     - 配列に以下の順に指令値を格納::

         0: right_track
         1: left_track
   * - 車両中心の並進移動速度/回転速度指令
     - ``/車体名/cmd_vel``
     - ``geometry_msg/msg/Twist``
     - 並進速度・角速度指令
   * - 非常停止
     - ``/車体名/emg_stop_cmd``
     - ``std_msgs/msg/Bool``
     - ``true``: その場で停止


Unity → ROS (建機の情報)
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: ブルドーザ: Unity → ROS (情報)
   :header-rows: 1
   :widths: 30 30 20 20

   * - 項目
     - トピック名
     - メッセージ型
     - 備考
   * - 各関節の角度, 角速度
     - ``/車体名/joint_states``
     - ``sensor_msgs/msg/JointState``
     - 以下の順で情報が格納される::

         0: lift_joint
         1: tilt_joint
         2: angle_joint
         3: right_track_joint
         4: left_track_joint
   * - ローカル座標系における車両の中心姿勢
     - ``/車体名/odom_pose``
     - ``nav_msgs/msg/Odometry``
     - -
   * - グローバル(平面直角)座標系における車両の中心姿勢
     - ``/車体名/global_pose``
     - ``nav_msgs/msg/Odometry``
     - 
   * - 油圧アクチュエータのメイン圧力
     - ``/車体名/main_fluid_pressure``
     - ``com3_ros/sensor_msgs/FluidPressure``
     - 以下の順で情報が格納される::

         0: lift_up_main_pressure
         1: lift_down_main_pressure
         2: tilt_forward_main_pressure
         3: tilt_back_main_pressure
         4: angle_right_main_pressure
         5: angle_left_main_pressure
   * - 油圧アクチュエータのパイロット圧力
     - ``/車体名/main_fluid_pressure``
     - ``com3_ros/sensor_msgs/FluidPressure``
     - 以下の順で情報が格納される::

         0: lift_up_pilot_pressure
         1: lift_down_pilot_pressure
         2: tilt_forward_pilot_pressure
         3: tilt_back_pilot_pressure
         4: angle_right_pilot_pressure
         5: angle_left_pilot_pressure
   * - 上部構造体の旋回角度
     - ``/車体名/upper_body_rot``
     - ``sensor_msggs/msg/Imu``
     - -


備考
----

* いずれの建機モデルも Pub/Sub 方式で通信します。
* 上記表中の「車体名」は、建設機械モデルのルート GameObject 名で置き換えてください
  (例: ``/zx120/front_cmd``, ``/ic120/track_cmd`` など)。


オプション: Movement Control Type / Control Type
-----------------------------------------------

建設機械モデルは ROS 通信で受け取った指令に応じて動作します。
入力としては、次の 3 種類の **Movement Control Type** をサポートします。

.. list-table:: Movement Control Type
   :header-rows: 1
   :widths: 30 70

   * - 項目
     - 説明
   * - Actuator Command
     - 建設機械の各関節それぞれに対して直接動作指令を行う
   * - Twist Command
     - 建設機械の移動速度・旋回速度を指定する
   * - Volume Command
     - 建設機械の移動速度・旋回速度を比率 (``-1.0 ~ 1.0``) で指定する

Actuator Command については、さらに次の 3 種類の **Control Type** を選択できます。

.. list-table:: Control Type
   :header-rows: 1
   :widths: 30 70

   * - 項目
     - 説明
   * - Position
     - 関節の角度の変化量を入力する
   * - Speed
     - 関節が移動する角速度を入力する
   * - Force
     - 関節が接続しているパーツに対して発生する力を入力する

各建設機械モデルがどのパターンの入力を受け取るかは、
Unity Editor のインスペクタから設定できます。

1. Hierarchy ビューで ``MACHINES`` に配置されている建設機械モデルを選択する
2. ``???Input`` という名前のスクリプトがアタッチされていることを確認する
   (``???`` には ``Excavator``, ``Dumptruck``, ``Bulldozer`` などのモデル名が入る)
3. ``Movement Control Type`` を選択する
4. ``Control Type`` を選択する


入力パターンと対応トピック
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 各モデルの対応パターンとトピック
   :header-rows: 1
   :widths: 20 25 15 40

   * - モデル
     - パターン
     - 対応状況
     - トピック名
   * - 油圧ショベル
     - Actuator Command
     - 対応
     - ``/車体名/front_cmd``, ``/車体名/track_cmd``
   * - 油圧ショベル
     - Twist Command
     - 対応
     - ``/車体名/cmd_vel``
   * - 油圧ショベル
     - Volume Command
     - 未対応
     - ``-``
   * - クローラダンプ
     - Actuator Command
     - 対応
     - ``/車体名/rot_dump_cmd``, ``/車体名/track_cmd``
   * - クローラダンプ
     - Twist Command
     - 対応
     - ``/車体名/cmd_vel``
   * - クローラダンプ
     - Volume Command
     - 対応
     - ``/車体名/track_volume_cmd``
   * - ブルドーザ
     - Actuator Command
     - 対応
     - ``/車体名/blade_cmd``, ``/車体名/track_cmd``
   * - ブルドーザ
     - Twist Command
     - 対応
     - ``/車体名/cmd_vel``
   * - ブルドーザ
     - Volume Command
     - 未対応
     - ``-``
