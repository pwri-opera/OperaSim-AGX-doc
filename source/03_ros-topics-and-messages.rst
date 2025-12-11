ROSと連携時の送受信データ
===========================

建機へのコマンド(ROS -> Unity) 
-------------------------------

.. list-table::

    * - データの内容
      - トピック名
      - トピック型
      - 物理量
      - 単位
      - 備考
    * - 建機の移動体部に対する対地速度指令値
      - /(建機のns)/tracks/cmd_vel
      - geometry_msgs/Twist
      - 速度
      - [m/s],[rad/s]
      -
    * - ダンプトラックの荷台の傾斜角指令値
      - /(建機のns)/vessel/cmd
      - std_msgs/Float64
      - 角度
      - [rad]
      -
    * - 建機のスイング軸の角度指令値
      - /(建機のns)/swing/cmd
      - std_msgs/Float64
      - 角度
      - [rad]
      -
    * - 建機のブーム軸の角度指令値
      - /(建機のns)/boom/cmd
      - std_msgs/Float64
      - 角度
      - [rad]
      -
    * - 建機のアーム軸の角度指令値
      - /(建機のns)/arm/cmd
      - std_msgs/Float64
      - 角度
      - [rad]
      -
    * - 建機のバケット軸の角度指令値
      - /(建機のns)/bucket/cmd
      - std_msgs/Float64
      - 角度
      - [rad]
      -



建機の情報の取得(Unity -> ROS)
--------------------------------

.. list-table::

    * - データの内容
      - トピック名
      - トピック型
      - 物理量
      - 単位
      - 備考
    * - 建機のベースリンクの座標
      - /(建機のns)/base_link/pose
      - geometry_msgs/PoseStamped
      - 位置・姿勢
      - 位置:[m]  姿勢:[-]
      - Unity内のworld座標系に対する座標の真値 |
    * - 建機のオドメトリ計算結果
      - /(建機のns)/odom
      - nav_msgs/Odometry
      - オドメトリ
      - 位置:[m]  姿勢:[-]
      - 初期位置を原点として算出している
    * - 建機の関節角度・角速度
      - /(建機のns)/joint_states
      - sensor_msgs/JointState
      - 角度・角速度
      - 角度:[rad]  角速度:[rad/s]
      - effortについては次節を参照
    * - 建機のIMUセンサ
      - /(建機のns)/(関節部位)/g2_imu
      - sensor_msgs/JointState
      - 角度・角速度
      - 角度:[rad]  角速度:[rad/s]
      - effortについては次節を参照
    * - 建機のGNSSセンサ
      - /(建機のns)/gnss_compass/fix
      - sensor_msgs/JointState
      - 角度・角速度
      - 角度:[rad]  角速度:[rad/s]
      - effortについては次節を参照
    * - 建機のGNSSセンサ
      - /(建機のns)/gnss_compass/heading
      - geometry_msgs/QuaternionStamped
      - 時刻・座標
      - 時間[sec:nsec]・位置:[m]
      - effortについては次節を参照
    * - unityの基準時計
      - /clock
      - rosgraph_msgs/Clock
      - 時刻
      - 時間[sec:nsec]
      - effortについては次節を参照



関節トルクセンサの有効化
--------------------------

各ゲームオブジェクトに設定された `Joint State Publisher` スクリプトの `Enable Joint Effort Sensor` をチェックすることで、joint_statesトピックからeffort値を出力させることができます。

.. image:: https://cdn.statically.io/gh/pwri-opera/OperaSim-PhysX/main/images/enable_joint_effort_sensor.png

.. note::

    関節トルクセンサは実機では利用できないことが多いのでご注意ください。
    OPERAが提供している実機では、関節トルクセンサを利用できません。

