概説
=====

- 本シミュレータは自律施工技術開発基盤OPERA（Open Platform for Earth work with Robotics and Autonomy）の一部であり、どなたでも利用可能です
- 油圧ショベル, クローラダンプ, ブルドーザと土砂の挙動を再現したシミュレータです
- シミュレータプラットフォームに `Unity <https://unity.com/>`_ 、物理エンジンに `AGX Dynamics(Algoryx Simulation ABが開発) <https://www.algoryx.se/agx-dynamics/>`_ を利用しています
- Unityを利用するため、利用者が所属する組織に応じたUnityのライセンスが必要です。詳細は `Unityの公式サイト <https://store.unity.com/ja>`_ をご確認の上、利用登録をしてください。
- AGX Dynamicsを利用するため、シミュレーションの実行には以下のモジュールのライセンスが必要です。詳細は販売代理店へ確認の上、ライセンスを入手してください。

   - AGX Dynamics Core 
   - AGX Dynamics Terrain
   - AGX Dynamics Granular
   - AGX Dynamics Tracks
  
- ROSメッセージを使って本シミュレータの建設機械を制御することができます
- 本シミュレータから建設機械の情報(関節の角度など)を含んだROSメッセージとして出力することが可能です
- ROSメッセージの送受信に `ROS-TCP-Connector <https://github.com/Unity-Technologies/ROS-TCP-Connector>`_ を使用します

.. .. image:: https://user-images.githubusercontent.com/24404939/159425467-c244de28-354e-4d2a-a615-5ccafc7b9709.gif

.. only:: html

   .. raw:: html

      <video controls autoplay loop muted playsinline width="640">
        <source src="_static/media/OperaSimAgxPromotion.mp4" type="video/mp4">
        お使いのブラウザでは動画を再生できません。
      </video>

++++

ソフトウェア要件
=====

- Unity：2022.3.62f1
- AGX：2.38.0.1(X64 VS2022)
   - AGX (Core)
   - Granular
   - Terrain
   - Tracks

Unityで使用するパッケージ
-----------------------------------

初回プロジェクト読み込み時に自動的に追加される.  
(もしも追加されなかった場合は手動で追加すること)

- `AGXUnity <https://github.com/Algoryx/AGXUnity>`_ : 5.0.1 
- `ROS-TCP-Connector <https://github.com/Unity-Technologies/ROS-TCP-Connector>`_ : 0.7.0 
- `URDF-Importer <https://github.com/Unity-Technologies/URDF-Importer>`_ : 0.5.2
- `UnitySensors <https://github.com/Field-Robotics-Japan/UnitySensors>`_ : 開発版 
