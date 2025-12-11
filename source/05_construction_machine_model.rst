
建機モデルの追加方法
===============================

既存の重機モデルを追加する方法
------------------------------------------

【サンプルモデルの例：12t油圧ショベルzx120の場合】

| ============================================================
| １．既に構築済の建設機械のシミュレーションモデル（GameObject）を 
|      Prefab化して再利用する方法
| ============================================================

１－１．既存の建機モデル（GameObject）のエクスポート（Prefabの作成）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　1-1 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/prefab-01.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | Hierarchy上からPrefab化したい建機モデルを選択する
       | 例：zx120の場合

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　1-2 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/create_prefab.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | ProjectウィンドウよりAssets/Prefabフォルダを
       | 選択しドラッグ＆ドロップする

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　1-3 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/prefab_file.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - prefabファイル(zx120.prefab)がAssets/Prefabフォルダ下に作成される

１－２．作成したprefabファイルを同一プロジェクトへインポートする
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　1-4 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/prefab_use.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | ProjectウィンドウのAssets/Prefabフォルダから配置したい建機の
       | prefabファイルを選択しScene上へドラッグ＆ドロップする

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　1-5 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/prefab_rename.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | Sceneビュー上で建機モデルの配置を調整し
       | Inspectorウィンドウ上のObject名を固有のものへ修正する

３Dメッシュアッセンブリデータ（.urdf）を基に重機モデルを新規作成する方法
-------------------------------------------------------------------------


.. 油圧ショベル
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

【例：12t油圧ショベルzx120の場合】

２－１．URDF Importerパッケージの追加
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-1 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/prefab-17.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - unity editor から「Window」「Package Manager」を選択する


.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-2 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/prefab-18.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | 「Package Manager」ウインドウから「+」
       | 「Add package from git URL...」を選択する


.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-3 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/prefab-19.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | 「Package Manager」ウインドウから「下記のURL」を入力し
       | 「Add」を選択する

========= =========================================================================================================
  ＵＲＬ    https://github.com/Unity-Technologies/URDF-Importer.git?path=/com.unity.robotics.urdf-importer#v0.5.2
========= =========================================================================================================

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-4 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/prefab-21.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - URDF Importerをインストール中の画面

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-5 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/prefab-22.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - URDF Importerがパッケージリスト上にあることを確認する

２－２．重機の３D形状アッセンブリデータ(zx120.urdf)をインポートする
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-6 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/urdf_importer.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | ProjectウィンドウからAssets/Machines/zx120フォルダ
       | にあるzx120(.urdf)を右クリックして表示されるリストから
       | 「Import Robot from Selected URDF file」を選択する


.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-7 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/prefab-24.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | 「URDF import Setting」タブから『Y Axiss』『VHACD』を選択し
       | 「Import URDF」を選択する

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-8 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/imported_urdf.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - zx120の形状モデルがScene上に現れたことを確認する


２－３．建機モデルを動作させるための諸設定
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-9　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_object_tree.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | Hierarchyウィンドウ上でインポートしたオブジェクトのツリーを展開して表示する
       | （zx120 - base_link - body_link - boom_link - arm_link-bucket_link - bucket_end_link）

zx120のルートオブジェクトへのコンポーネント追加とパラメータセッティング

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-10 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_object_components.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | zx120のルートオブジェクト"zx120"を選択し
       | Inspectorウィンドウより「Add Component」
       | をクリックして必要なコンポーネントを追加する
       | またController(Script)のチェックボックスを外す

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-11 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_object_setting1.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | 各種Componentのパラメータを設定する
       | Joint State Publisher, Follow Joint Trajectory(左)
       | Diff Drive Controller(右)
       | 各コンポーネント, パラメータについては説明割愛

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-12 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_object_setting2.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | 各種Componentのパラメータを設定する
       | Rigidbody, Box Collider(左)
       | Fixed Joint, Custom Collision ZX120(右)
       | 各コンポーネント, パラメータについては説明割愛

zx120のbase_linkオブジェクトへのコンポーネント追加とパラメータセッティング

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-13 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_base_link_components.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | zx120の子であるbase_linkオブジェクトをHierarchyウィンドウより選択し
       | Inspectorウィンドウより「Add Component」
       | をクリックして必要なコンポーネントを追加する
       | またController(Script)のチェックボックスを外す

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-14 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_base_link_object_setting.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | base_linkにアタッチした各種Componentのパラメータを設定する
       | ArticulationBody, Urdf Inertial
       | Pose Stamped Publisher
       | 各コンポーネント, パラメータについては説明割愛

zx120のbody_linkオブジェクトへのコンポーネント追加とパラメータセッティング

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-15 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_body_link_components.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | base_linkの子であるbody_linkオブジェクトをHierarchyウィンドウより選択し
       | Inspectorウィンドウより「Add Component」
       | をクリックして必要なコンポーネントを追加する
       | またController(Script)のチェックボックスを外す

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-16 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_body_link_object_setting.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | body_linkにアタッチした各種Componentのパラメータを設定する
       | ArticulationBody, Joint Pos Controller
       | 各コンポーネント, パラメータについては説明割愛

zx120のboom_linkオブジェクトへのコンポーネント追加とパラメータセッティング

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-17 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_boom_link_components.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | body_linkの子であるboom_linkオブジェクトをHierarchyウィンドウより選択し
       | Inspectorウィンドウより「Add Component」
       | をクリックしてJoint Pos Controllerを追加する

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-18 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_boom_link_object_setting.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | boom_linkにアタッチした各種Componentのパラメータを設定する
       | Transform
       | ArticulationBody, Joint Pos Controller
       | 各コンポーネント, パラメータについては説明割愛

zx120のarm_linkオブジェクトへのコンポーネント追加とパラメータセッティング

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-19 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_arm_link_components.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | boom_linkの子であるarm_linkオブジェクトをHierarchyウィンドウより選択し
       | Inspectorウィンドウより「Add Component」
       | をクリックしてJoint Pos Controllerを追加する

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-20 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_arm_link_object_setting.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | arm_linkにアタッチした各種Componentのパラメータを設定する
       | Transform
       | ArticulationBody, Joint Pos Controller
       | 各コンポーネント, パラメータについては説明割愛

zx120のbucket_linkの不要ジオメトリの削除

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-21 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_bucket_link_object_delete.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | bucket_linkの子であるCollisionsオブジェクトをHierarchyウィンドウより全て削除する
       | 同様にVisualsオブジェクト中のarm-bk-dmおよびbk-C-dmを削除する

zx120のbucket_linkの粒子保持用干渉形状の生成

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-22 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_bucket_link_add_collider.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | Collisionsオブジェクトに残ったbakeオブジェクトに
       | SA Mesh Collider Builderスクリプトをアタッチする
       | https://assetstore.unity.com/packages/tools/sacolliderbuilder-15058

zx120のbucket_linkの粒子保持用干渉形状の生成

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-23 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_bucket_link_process_collider.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | SA Mesh Collider Builder上からprocessを左クリックして
       | Herarchy上のbacketオブジェクト以下に「Prim.***」という
       | 矩形オブジェクトが多数生成されることを確認する

zx120のbucket_linkの粒子生成用干渉形状の生成

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-24 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_bucket_link_add_collider.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | bucket_innerについて 
       | （松坂さん、作成方法の手順について追記お願いします） 

２－４．移動体（クローラ）部を6輪スキッドステアとしてモデル化する方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

zx120のルートオブジェクトに空オブジェクトのwheelsを追加する

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-25 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_add_wheels_object.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | zx120のルートオブジェクトをHierarchyウィンドウより選択し
       | 右クリックで表示されるリストから「Create Empty」を選択し
       | Inspector上でオブジェクト名をwheelsとする
       | またLayerを「Ignore Collision」に設定する

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-26 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_add_wheel_link_objects.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | wheelsオブジェクトに対し、6つのEmptyオブジェクトを追加し
       | それぞれ名称を「right_rear_wheel_link」「right_middle_wheel_link」
       | 「right_front_wheel_link」「left_rear_wheel_link」
       | 「left_middle_wheel_link」「left_front_wheel_link」に設定する

.. list-table::
   :widths: 15 30
   :header-rows: 1

   * - 図　2-27 　[拡大]
     - 内容
   * - .. image:: construction_machine_model/img/zx120_wheel_object_config.png
          :scale: 100%
          :height: 100px
          :width: 200px
     - | 追加した各**_wheel_linkに対しInspector上で「Add Component」より
       | 「Wheel Collider」を追加しTransform, WheelColliderにそれぞれ
       | 適切にパラメータを設定する
       | 各コンポーネント, パラメータについては説明割愛

２－５．油圧ショベルのシミュレーションのため各オブジェクトにアタッチされるコンポーネントの一覧                                                        +
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-------------+-------------------------+---------+---------------------------+
| Layer Depth | Game Object Name        |  Active | Component                 |
+-------------+-------------------------+---------+---------------------------+
| 0           | zx120                   |   〇    | Transform                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Urdf Robot                |
+             +                         +---------+---------------------------+
|             |                         |         | Controller                |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Joint State Publisher     |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Follow Joint Trajectory   |
+             +                         +---------+---------------------------+
|             |                         |   〇    | DiffDriveController       |
+             +                         +---------+---------------------------+
|             |                         |         | Rigidbody                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Box Collidar              |
+             +                         +---------+---------------------------+
|             |                         |         | Fixed Joint               |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Custom Collision ZX120    |
+-------------+-------------------------+---------+---------------------------+
| 1           | base_link               |   〇    | Transform                 |
+             +                         +---------+---------------------------+
|             |                         |         | Urdf Link                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Articulation Body         |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Urdf Inertial             |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Pose Stamped Publisher    |
+-------------+-------------------------+---------+---------------------------+
| 2           | body_link               |   〇    | Transform                 |
+             +                         +---------+---------------------------+
|             |                         |         | Urdf Link                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Articulation body         |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Urdf Inertial             |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Urdf Joint Continuous     |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Joint Pos Controller      |
+-------------+-------------------------+---------+---------------------------+
| 3           | boom_link               |   〇    | Transform                 |
+             +                         +---------+---------------------------+
|             |                         |         | Urdf Link                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Articulation body         |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Urdf Inertial             |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Urdf Joint Revolute       |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Joint Pos Controller      |
+-------------+-------------------------+---------+---------------------------+
| 4           | arm_link                |   〇    | Transform                 |
+             +                         +---------+---------------------------+
|             |                         |         | Urdf link                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Articulation body         |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Urdf Inertial             |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Urdf Joint Revolute       |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Joint Pos Controller      |
+-------------+-------------------------+---------+---------------------------+
| 5           | bucket_link             |   〇    | Transform                 |
+             +                         +---------+---------------------------+
|             |                         |         | Urdf link                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Articulation body         |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Urdf Inertial             |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Urdf Joint Revolute       |
+             +                         +---------+---------------------------+
|             |                         |         | SA Mesh Collider Builder  |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Joint Pos Controller      |
+-------------+-------------------------+---------+---------------------------+
| 1           | wheels                  |   〇    | Transform                 |
+-------------+-------------------------+---------+---------------------------+
| 2           | left_rear_wheel_link    |   〇    | Urdf link                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Wheel Collider            |
+-------------+-------------------------+---------+---------------------------+
| 2           | left_middle_wheel_link  |   〇    | Urdf link                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Wheel Collider            |
+-------------+-------------------------+---------+---------------------------+
| 2           | left_front_wheel_link   |   〇    | Urdf link                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Wheel Collider            |
+-------------+-------------------------+---------+---------------------------+
| 2           | right_rear_wheel_link   |   〇    | Urdf link                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Wheel Collider            |
+-------------+-------------------------+---------+---------------------------+
| 2           | right_middle_wheel_link |   〇    | Urdf link                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Wheel Collider            |
+-------------+-------------------------+---------+---------------------------+
| 2           | right_front_wheel_link  |   〇    | Urdf link                 |
+             +                         +---------+---------------------------+
|             |                         |   〇    | Wheel Collider            |
+-------------+-------------------------+---------+---------------------------+


クローラダンプ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
油圧ショベルと同様の手順で作成する

ブルドーザ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TBD
