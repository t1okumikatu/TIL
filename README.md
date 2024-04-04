# TIL
「Today I Learned」の略で、Github上にTILというリポジトリを作成してそこに今日覚えたことを書いていく

パーソナル アクセス トークン（PAT）は、スクリプトの使用や外部アプリとアトラシアン アプリの連携を安全に行うために使用されます。外部システムが侵害された場合、トークンを取り消すだけで済みます。﻿

GitHub.comにパスワードレス認証の導入
Image of Hirsch Singhal
Hirsch Singhal

パスキーがパブリックベータ版にて利用が可能になりました。オプトインすることで、セキュリティキーをパスキーにアップグレードし、パスワードと2FA方式の代わりにパスキーを使用することができます。


***//修正

motor_drive_2.pyは右MOTORを＋１０UP

pi.set_PWM_dutycycle(MOT_R_1, 60) #MOT_R_1:50/100

pi.set_PWM_dutycycle(MOT_R_2, 0) #MOT_R_2:50/0

pi.set_PWM_dutycycle(MOT_L_1, 50) #MOT_L_1:50/100

pi.set_PWM_dutycycle(MOT_L_2, 0) #MOT_L_2:50/0


