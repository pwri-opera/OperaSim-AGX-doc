インストール方法
=================

1. Unity(ver:2022.3.4f1)のインストール
---------------------------------------

使用しているPCのOSに応じて以下の通りUnityHubをインストールする


- windows 又は Macの場合: https://unity3d.com/jp/get-unity/download
- Linuxの場合(Linux版は動作確認を実施しておりません): https://unity3d.com/get-unity/download

2. Projectファイルの開き方とUnity Editorのダウンロード
------------------------------------------------------

- UnityHubを起動し、画面右上の「追加」から `OperaSim-PhysX` (Githubから自身のPCにクローン又はダウンロードしたもの)を選択し、クリックする（初回起動時には数分程度の時間がかかります）。クリックした際に指定のUnity Editorを選択しインストールする。

3. Sceneファイルの選択
----------------------

- デモ用のサンプルSceneファイルが `Asset/Scenes/SampleScene.unity` にあるので、これを開く.  

4. ROS-TCP-Connectorの設定
--------------------------

- UnityEditorの上部ツールバーからRobotics > ROS Settingを開き"ROS IP Address", "ROS Port"のところにROS側のIPアドレスおよびポート番号(defaultは10000)を入力する
- もしROS2を利用する場合は"Protocol"のところを"ROS1"->"ROS2"へ変更する

.. image:: https://user-images.githubusercontent.com/24404939/159395478-46617a2f-b05c-4227-9fc9-d93712dc4b9f.jpg

5. ROSとの連携方法
------------------

.. image:: https://user-images.githubusercontent.com/24404939/161001271-0f81d211-4c8e-4341-8f9f-86a02e958c4d.jpg

- 【初回のみ】ROS側で `ROS-TCP-Endpoint <https://github.com/Unity-Technologies/ROS-TCP-Endpoint>`_ パッケージをcloneし、buildとセットアップを行う。

    ROS 1の場合:

        .. code-block:: console

            $ cd (rosワークスペース)/src
            $ git clone https://github.com/Unity-Technologies/ROS-TCP-Endpoint.git
            $ cd ./ROS-TCP-Endpoint/
            $ sudo chmod +x setup.py
            $ ./setup.py
            $ catkin build ros_tcp_endpoint
            $ source ../../devel/setup.bash

    ROS 2の場合:

        .. code-block:: console

            $ cd (ros2ワークスペース)/src
            $ git clone -b main-ros2 https://github.com/Unity-Technologies/ROS-TCP-Endpoint.git
            $ cd ./ROS-TCP-Endpoint/
            $ sudo chmod +x setup.py
            $ ./setup.py
            $ cd ../../
            $ colcon build --packages-select ros_tcp_endpoint
            $ . install/setup.bash

- ROS側でendpoint.launchを実行する

    .. code-block:: console

        $ roslaunch ros_tcp_endpoint endpoint.launch

- Unity Editor上部の実行ボタンをクリックする

    .. image:: https://user-images.githubusercontent.com/24404939/159396113-993ff0b2-d2bb-4567-ac68-0eafc9f524ac.png

- ROS側で、対応する建機のunity用launchファイルを起動する

    - 油圧ショベル

        .. code-block:: console

            $ roslaunch zx120_unity zx120_standby.launch

    - クローラダンプ

        .. code-block:: console

            $ roslaunch ic120_unity ic120_standby.launch
