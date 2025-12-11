
センサモデルの追加方法
===============================

Unity Sensorsパッケージのインストール方法
------------------------------------------
OperaSim-PhysXでは、Field-Robotics-Japanがオープンソースとして公開しているUnitySensorsパッケージを使用しています。

１．UnitySensors パッケージのインストール

ＩＭＵセンサを作成する前準備としてUnitySensors パッケージを追加インストールする

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　1-2 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-02.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - unity メニューバーから「Window」「Package Manager」を選択する
     
２．  Package Manager ウィンドウのメニューバーから「＋」「Add package from git URL」を選択する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　1-3 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-03.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Package Manager ウィンドウの例
   * - .. image:: imu_gnss/img/unity-04.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - メニューバーから「＋」「Add package from git URL」を選択する

３．Package Manager ウィンドウのＵＲＬ入力テキストボックスに下記のURLを入力し「Add」ボタンを押下する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　1-4 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-06.png
          :scale: 100%
          :height: 150px
          :width: 400px
     - Package Manager ウィンドウのＵＲＬ入力テキストボックスに

       下記のURLを入力し「Add」ボタンを押下する
   * - 入力するURL【※１】
     - https://github.com/Field-Robotics-Japan/UnitySensors.git?path=/Assets/UnitySensors#v2.0.4"

===================== =======================================================================
 【※１注意】          | UnitySensorsについては、
                      | 都度バージョンアップされる場合があります
                      | 下記のURL にて最新バージョンが公開されますが
                      | 適合するかどうかについては都度確認が必要です
 Assets/UnitySensors    https://github.com/Field-Robotics-Japan/UnitySensors
===================== =======================================================================

４．UnitySensors パッケージがインストールされることを確認する

.. list-table::
   :widths: 10 15
   :header-rows: 1

   * - 図　1-5 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-07.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - UnitySensors パッケージがインストールされる

５．UnitySensors パッケージが図の内容のようにインストールされたことを確認する

.. list-table::
   :widths: 10 15
   :header-rows: 1

   * - 図　1-6 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-08.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - UnitySensors パッケージがインストールされたことを確認する

６．UnitySensorsROS パッケージのインストール

Package Manager ウィンドウのメニューバーから再度、「＋」「Add package from git URL」を選択する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　1-7　[拡大] 
     - 操作
   * - .. image:: imu_gnss/img/unity-04.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - メニューバーから再度、「＋」「Add package from git URL」を選択する

７．Package Manager ウィンドウのＵＲＬ入力テキストボックスに下記のURLを入力し「Add」ボタンを押下する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　1-8 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-09.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Package Manager ウィンドウのＵＲＬ入力テキストボックスに

       下記のURLを入力し「Add」ボタンを押下する
   * - 入力するURL【※２】
     - https://github.com/Field-Robotics-Japan/UnitySensors.git?path=/Assets/UnitySensorsROS#v2.0.4 

===================== =======================================================================
 【※１注意】          | UnitySensorsについては、
                      | 都度バージョンアップされる場合があります
                      | 下記のURL にて最新バージョンが公開されますが
                      | 適合するかどうかについては都度確認が必要です
 Assets/UnitySensors   https://github.com/Field-Robotics-Japan/UnitySensors
===================== =======================================================================

８．UnitySensorsROS パッケージがインストールされる

.. list-table::
   :widths: 10 15
   :header-rows: 1

   * - 図　1-9 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-10.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - UnitySensorsROS パッケージをインストール中の画面

９．UnitySensorsROS パッケージが図1-10の通りであることを確認する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　1-10 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-11.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - UnitySensorsROS パッケージがインストールされたことを確認する

IMUセンサモデルの追加方法
--------------------------

１．実機のＩＭＵの取り付け位置確認

== =================================================================
　  シミュレーション内の建機モデルに対応する実機のＩＭＵの取り付け位置を現物確認する

    （図1-1：油圧ショベルzx120のアームリンク計測用IMU）
== =================================================================

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　1-1 　[拡大]
     - 内容
   * - .. image:: imu_gnss/img/IMG_2394.jpg
          :scale: 100%
          :height: 100px
          :width: 200px
     - 実機に取り付け位置を合わせるため、現物を確認する

ＩＭＵは、zx120の場合、キャビン、ブームリンク、アームリンク、バケットリンクに取りついている

.. .. list-table::
..   :widths: 10 80 30
..   :header-rows: 1

..   * - 番号
..     - 概要
..     - 記載項目
..   * - 1）
..     - 実機に取り付けられているIMUセンサについてUnity Editorでシミュレーションする
..     - 
..   * - 2）
..     - Unity Editor内のUnitySensorsパッケージをインストールする
..     - 2.へ
..   * - 3）
..     - それぞれのIMUセンサについてUnity Editor内のショベルモデルにGame Objectを作成する
..     - IMUセンサモデルの追加方法へ
..   * - 4）
..     - 実機ショベルで動作したIMUセンサデータを取得して動作データを解析する
..     - 
..   * - 5）
..     - 実機ショベルで動作したデータを分析し、シミュレーションに合致するように環境設定をする
..     - センサモデルの設定情報取得とIMUのデータ値設定
..   * - 6）
..     - ROS - Unity Editorにてシミュレーションを実施してROS側でデータを取得し、シミュレーションが正しく動作していることを確認する
..     - 

2．Unity Editorで空オブジェクトを作成

Unity Editor を起動し、ＩＭＵの空オブジェクトを作成する（例：boom_imu の場合）

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-1 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-01.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Unity Editorを起動する
   * - .. image:: /imu_gnss/img/unity-01-2.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - unity 「Hierarchy」タブから「zx120」「base_link」「body_link」「boom_link」

       を選択し右クリックで表示されるリストより「Create Empty」を選択する

=== ===========================================================
　  | boom_imu の場合、ショベルの実機写真（図　1-1 ）の通り
    | ショベルモデルのboom_link に対する空オブジェクトの原点
    | および姿勢を調整して合わせる
=== ===========================================================

３．「Inspector」タブで GameObjectに名称を設定する（例：boom_imu）

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-2 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-02-1.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - GameObjectに名称を設定する（例：boom_imu）


４．unity 「Hierarchy」タブから「boom_imu」を選択し「Inspector」タブを参照する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　2-3 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-15.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - unity 「Hierarchy」タブから「boom_imu」を選択し

       「Inspector」タブを参照する

５．「Inspector」タブから「Add Component」ボタンを押下し「IMU Sensor」を選択する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　2-4 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-16.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「Inspector」タブから「Add Component」ボタンを押下し

        「IMU Sensor」を選択する

６.「IMU Sensor」のコンポーネントが「Inspector」タブに追加されていることを確認する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　2-5 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-17.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「IMU Sensor」のコンポーネントが「Inspector」タブに

         追加されていることを確認する

７.再度「Inspector」タブから「Add Component」ボタンを押下し「IMU Msg Publisher 」を選択する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　2-6 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-18.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 再度「Inspector」タブから「Add Component」ボタンを押下し

       「IMU Msg Publisher 」を選択する

８.「IMU Msg Publisher」のコンポーネントが図のように「Inspector」タブに追加されていることを確認する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　2-7 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-19.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「IMU Msg Publisher」のコンポーネントが「Inspector」タブに

         追加されていることを確認する

９.「Inspector」上で、ROS topic名およびframe_idを実機に合わせ設定する

.. list-table::
   :widths: 10 15
   :header-rows: 1

   * - 図　2-8 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/imu_topic_frame_id_setting.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「Topic Name」「Frame_id」をそれぞれ設定する

10.Unity のPlay ボタンをクリックする

.. list-table::
   :widths: 10 15
   :header-rows: 1

   * - 図　2-9 
     - 操作
   * - .. image:: imu_gnss/img/unity-21.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Unity EditorのPlay 「▶」ボタンをクリックし
       
       シミュレーションを実行する

11.シミュレータからPublishされるIMUのROS topicを表示し、所望の出力が得られることを確認する

.. list-table::
   :widths: 10 15
   :header-rows: 1

   * - 図　2-10 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/imu_topic_echo.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - ROS側でrostopic echo 等を実行し、所望のROS topicとしてIMU出力が得られることを確認する

=== ================================================
　  | 同様の方法で、swing、arm、bucket について
    | ＩＭＵセンサモデルを追加し設定する
=== ================================================

GNSSセンサモデルの追加方法
--------------------------

１．ショベル実機のＧＮＳＳセンサの取り付け位置確認

=== ====================================================================
　  | シミュレーション内の建機モデルに対応する実機のGNSSの取り付け位置を現物確認する
    | （図1-1：油圧ショベルzx120のRTK GNSSコンパスHemisphere V500）
=== ====================================================================

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　3-1 　[拡大]
     - 内容
   * - .. image:: imu_gnss/img/GNSS-01.jpg
          :scale: 100%
          :height: 100px
          :width: 200px
     - 実機に取り付け位置を合わせるため、現物を確認する

=== ====================================================================
　  | ＧＮＳＳコンパスは、zx120のbodyリンク上に固定されている
=== ====================================================================


２．Unity Editorで空オブジェクトの作成

　　　Unity Editor を起動し、ＧＮＳＳの空オブジェクトを作成する

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　3-2 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/unity-01.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Unity Editor を起動する
   * - .. image:: /imu_gnss/img/gnss-02.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Unity Editor 「Hierarchy」タブから「zx120」「base_link」「body_link」

       を選択し右クリックで表示されるリストから「Create Empty」を選択する

３．「Inspector」タブで GameObjectに名称を設定する（例：gnss）

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　3-3 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/gnss-04.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - GameObjectに名称を設定する（例：gnss）


３．Unity Editor 「Hierarchy」タブから「gnss」を選択し「Inspector」タブを参照する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　3-4 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/gnss-05.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Unity Editor 「Hierarchy」タブから「gnss」を選択し

       「Inspector」タブを参照する

４．「Inspector」タブから「Add Component」ボタンを押下し「gnss」を選択する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　3-5 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/gnss-06.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「Inspector」タブから「Add Component」ボタンを押下し

       「GNSS Sensor」を選択する

５.「GNSS Sensor」のコンポーネントが図のように「Inspector」タブに追加されていることを確認する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　3-6 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/gnss-07.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「GNSS Sensor」のコンポーネントが「Inspector」タブに

         追加されていることを確認する

６.再度「Inspector」タブから「Add Component」ボタンを押下し「Nav Sat Fix Msg Publisher」を選択する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　3-7 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/gnss-09-2.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 再度「Inspector」タブから「Add Component」ボタンを押下し

       「Nav Sat Fix Msg Publisher」を選択する

７.「Nav Sat Fix Msg Publisher」のコンポーネントが図のように「Inspector」タブに追加されていることを確認する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　3-8 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/gnss-09-1.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「Nav Sat Fix Msg Publisher」のコンポーネントが

       「Inspector」タブに追加されていることを確認する

８. 再度「Inspector」タブから「Add Component」ボタンを押下し「Quaternion Stamped Publisher」を選択し、各パラメータを設定する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　3-9 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/compass_setting.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 実機のCompassの出力に合わせ

        Frame IDをmap

        Topic Nameをzx120/gnss_compass/heading

        Publish Message Intervalを0.09[s]

       にそれぞれ設定した様子

TerrainへGNSS座標の基準点を設定する
--------------------------------------------------------------------------

１．Unity Editor の「Hierarchy」タブから「Terrain」を選択し「Inspector」タブを開く

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　4-1 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/terrain-01-1.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「Terrain」コンポーネント

２．Unity EditorでTerrainコンポーネント上に空オブジェクトを作成する

Unity Editor を起動し、「Terrain」を右クリックで表示されるリストより「Create Empty」を選択する

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　4-2 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/terrain-02-1.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Unity Editor 「Hierarchy」タブから「Terrain」を選択し

        「Create Empty」にて空オブジェクトを追加する


３．「Inspector」タブで GameObjectに名称を設定する（例：GeoCoordinateSystem）

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　4-3 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/terrain-03-1.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - GameObjectに名称を設定する（例：GeoCoordinateSystem）


４．「Inspector」タブから「Add Component」ボタンを押下し「Geo Coordinate System」を選択する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　4-5 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/terrain-04-1.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「Inspector」タブから「Add Component」ボタンを押下し

        「Geo Coordinate System」を選択する

５.「Geo Coordinate System」の座標系の原点位置・姿勢および原点の緯度・経度・高度を設定する

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　4-6 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/gnss_coordinate_setting.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 当該座標系原点の位置

       （Latitute:緯度[度]、Longitude:経度[度]、Altitude:高度[m]）
       
       を入力する

       この場所を基準として、GNSSモデルの位置情報が

       NavSatFix型のROS topicとしてpublishされる

６.UnityのPlay ボタンをクリックする

.. list-table::
   :widths: 10 15
   :header-rows: 1

   * - 図　4-7 
     - 操作
   * - .. image:: imu_gnss/img/unity-21.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Unity EditorのPlay 「▶」ボタンをクリックし
     
       シミュレーションを実行する

７.ショベルモデルを移動させGNSSの位置（緯度、経度、高度）およびコンパスの方位が適切に変化することを確認する

.. list-table::
   :widths: 10 15
   :header-rows: 1

   * - 図　4-8 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/gnss-11-3-1.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - シミュレータを再生する（動作前）
   * - .. image:: imu_gnss/img/gnss-11-2-1.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - ショベルモデルを動作させる（動作後）

   * - .. image:: imu_gnss/img/gnss-11-1-1.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 対応するROS Topic（例：/zx120/gnss_compass/fix, /heading）
     
       が重機の動作に合わせて正しく変化していることを確認する

LiDARセンサモデルの追加方法
--------------------------------------------------------------------------
（注意）2025.2時点ではOPERAの建機に常設のLiDARセンサはありません

1．Unity Editorで空オブジェクトの作成

　　　Unity Editor を起動し、LiDAR用の空オブジェクトを作成する

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　5-1 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/add_empty_for_lidar.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Unity Editor 「Hierarchy」タブから「zx120」「base_link」「body_link」

       を選択し右クリックで表示されるリストから「Create Empty」を選択する

   * - .. image:: imu_gnss/img/rename_lidar.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Unity Editor 「Inspector」上で作成したGameObjectの名前を任意に変更する

       例）GameObject →　lidar1

２．LiDARセンサモデルの取付け位置を変更する

.. list-table::
   :widths: 15 30
   :header-rows: 1  

   * - 図　5-2 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/set_position_lidar.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Editor上のMove tool, Rotate tool, 「Inspector」上のTransformへ
    
       値をキーボード入力する、などを用いてbody_link上への

       LiDARモデルの固定位置を決定する


３．lidar1オブジェクトにLiDARのセンサprefabをアタッチする（例：Velodyne VLP-16）

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　5-3 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/attatch_lidar_prefab.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - ProjectウィンドウのPackages/UnitySensors/Runtime/Prefabs/LiDAR/Velodyne
     
       フォルダから配置したいLiDARのprefabファイルを選択し「Hierarchy」上の
       
       オブジェクト「lidar1」へドラッグ＆ドロップする　（例：VLP-16）

４．LiDARセンサモデルの各種コンフィギュレーション

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　5-4 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/lidar_config.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「Hierarchy」上からアタッチしたVLP-16 prefab下の「Sensor」オブジェクトを
     
       左クリックで選択し「Inspector」より「Raycast LiDAR Sensor」スクリプトの
      
       設定値を必要に応じて任意に変更する

       （各パラメータ説明については割愛）

５. LiDARセンサモデルのROSメッセージ出力機能の追加

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　5-5 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/add_pc2_msg_publisher.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「Sensor」オブジェクトを選択し、「Inspector」から「Add Component」より
    
       「Raycast LiDAR Point Cloud 2 Msg Pulisher」を追加する

   * - .. image:: imu_gnss/img/pc2_msg_publisher_setting.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「Hierarchy」上からアタッチした
     
       Raycast LiDAR Point Cloud 2 Msg Pulisher下の
     
       Topic Name（=ROSメッセージとして出力する際のトピック名）
      
       Header/Frame_id(=センサデータの基準時座標系名)

       をそれぞれ任意に設定する（例：いずれもzx120/lidar1）

RGBイメージセンサ（=カメラ）モデルの追加方法
--------------------------------------------------------------------------
（注意）2025.2時点ではOPERAの建機に常設のカメラはありません

1．Unity Editorで空オブジェクトの作成

Unity Editor を起動し、カメラ用の空オブジェクトを作成する

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　6-1 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/add_empty_for_cam.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Unity Editor 「Hierarchy」タブから「zx120」「base_link」「body_link」

       を選択し右クリックで表示されるリストから「Create Empty」を選択する

   * - .. image:: imu_gnss/img/rename_cam.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Unity Editor 「Inspector」上で作成したGameObjectの名前を任意に変更する

       例）GameObject →　cam1

２．カメラモデルの取付け位置を変更する

.. list-table::
   :widths: 15 30
   :header-rows: 1  

   * - 図　6-2 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/set_position_cam.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - Editor上のMove tool, Rotate tool, 「Inspector」上のTransformへ
    
       値をキーボード入力する、などを用いてbody_link上への

       カメラモデルの固定位置を決定する


３．cam1オブジェクトにカメラセンサのprefabをアタッチする（例：RGBカメラ）

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　6-3 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/attatch_rgbcam_prefab.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - ProjectウィンドウのPackages/UnitySensors/Runtime/Prefabs/Camera/RGBCamera
     
       フォルダから配置したいprefabファイルを選択し「Hierarchy」上の
       
       オブジェクト「cam1」へドラッグ＆ドロップする　（例：RGBCamera）

４．カメラセンサモデルの各種コンフィギュレーション

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　6-4 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/rgbcam_config.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「Hierarchy」上からアタッチしたRGBCamera prefabを
     
       左クリックで選択し「Inspector」より「Camera」「RGB Camera Sensor」
      
       スクリプトの設定値を必要に応じて任意に変更する

       （各パラメータ説明については割愛）

５. カメラセンサモデルのROSメッセージ出力機能の追加

.. list-table::
   :widths: 15 10
   :header-rows: 1

   * - 図　6-5 　[拡大]
     - 操作
   * - .. image:: imu_gnss/img/add_cam_image_msg_publisher.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「RGBCamera」オブジェクトを選択し、「Inspector」から「Add Component」より
    
       「Camera Image Msg Pulisher」を追加する

   * - .. image:: imu_gnss/img/cam_image_msg_publisher_setting.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - 「Hierarchy」上からアタッチした
     
       Camera Image Msg Pulisher下の
     
       Topic Name（=ROSメッセージとして出力する際のトピック名）
      
       Header/Frame_id(=センサデータの基準時座標系名)

       をそれぞれ任意に設定する（例：いずれもzx120/cam1）