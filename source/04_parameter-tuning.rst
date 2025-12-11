パラメータのチューニング方法
=============================

関節制御パラメータのチューニング
-----------------------------------

各関節の制御パラメータは、ゲームオブジェクトのXDriveパラメータを変更することで可能です。

.. image:: https://cdn.statically.io/gh/pwri-opera/OperaSim-PhysX/main/images/joint_properties.png

.. list-table::

    * - プロパティ名
      - 説明
    * - Lower Limit
      - 関節可動角の下限（単位はdegree）。可動角制限を有効にするには、Motionプロパティを「Limited」に設定してください
    * - Upper Limit
      - 関節可動角の上限（単位はdegree）。可動角制限を有効にするには、Motionプロパティを「Limited」に設定してください
    * - Stiffness
      - 関節の剛性係数。係数の意味は下の式を参照。0の場合はデフォルト値20000を使用します
    * - Damping
      - 関節の減衰係数。係数の意味は下の式を参照。0の場合はデフォルト値10000を使用します
    * - Force Limit
      - 制御中に加えられるトルクの最大値（単位はnewton）。0の場合はデフォルト値10000を使用します

Stiffness（剛性）とDamping（減衰）の各係数は、下の式に用いられます。

.. code::

    加えられるトルク = 剛性係数 * (駆動位置 - ターゲット位置) - 減衰係数 * (駆動速度 - ターゲット速度)

上記、各パラメータの詳しい説明は、Unityの公式マニュアルを参照ください。

https://docs.unity3d.com/ja/2023.2/Manual/class-ArticulationBody.html#joint-drive-properties

関節制御が振動的になった際のシミュレーションパラメータのチューニング
------------------------------------------------------------------------

長いリンクのある多関節の重機をシミュレーションする際に、関節制御が振動的になることがあります。
この症状は、以下の調整を行うことで軽減できます。

メニューから `Edit > Project Settings...` を選択し `Physics` 項目を選択します。

.. image:: https://cdn.statically.io/gh/pwri-opera/OperaSim-PhysX/main/images/physics_properties.png

`Default Solver Iterations` プロパティの数値を大きな値に変更してください。

粒子シミュレーションの挙動の調整
-----------------------------------

土砂の粒子シミュレーションのパラメータは、TerrainゲームオブジェクトのSoil Particle Settingで変更できます。

.. image:: https://cdn.statically.io/gh/pwri-opera/OperaSim-PhysX/main/images/soil_particle_setting.png

.. list-table::

    * - プロパティ名
      - 説明
    * - Enable
      - 土砂の粒子シミュレーションをオフにしたい時には、このチェックボックスのチェックを外してください。
    * - Particle Visual Radius
      - 粒子の見た目上の半径を設定します。粒子同士が干渉する半径を設定するには、下のRockPrefabの設定も合わせて調整してください。
    * - Particle Stick Distance
      - 近くの粒子との間に引力を働かせることで、土砂の粘性を再現できます。引力を発生させる範囲を設定します。
    * - Stick Force
      - 近くの粒子との間に発生させる引力の強さを設定します。

粒子が周囲の粒子と干渉する半径を調整するには、RockPrefabのSphere ColliderのRadius値を変更してください。

.. image:: https://cdn.statically.io/gh/pwri-opera/OperaSim-PhysX/main/images/soil_particle_collision_radius.png

センサシミュレーションのパラメータチューニング
-----------------------------------------------

IMU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GNSS Compass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

光学カメラ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

LiDAR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


