# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Harime",color="#9633FF")
define e2 = Character("Harime",color="#9633FF",image="qa")
define e3 = Character("Harime",color="#9633FF",image="qa")
define e4 = Character("Harime",color="#9633FF",image="qa")
define a = Character("[playername]",color="#33D7FF",image="tui")
define a2 = Character("[playername]",color="#33D7FF",image="tui")
define b = Character("Kẻ Bắt Nạt",color="#ff0303",image="buller")
image side tui = im.Scale("side tui.png",730,850)
image side tui2 = im.Scale("side tui2.png",730,850)
image side luxury = im.Scale("side luxury.png",340,400)
image side qa = im.Scale("side qa.png",700,850)
image side qa3 = im.Scale("side qa3.png",700,850)
image side qa2 = im.Scale("side qa2.png",700,850)
image side qa1 = im.Scale("side qa1.png",850,1050)
image side buller = im.Scale("side buller.png",430,580,xoffset=50,yoffset=-200)
image buller = im.Scale("buller.png",520,750)
image buller1 = im.Scale("buller1.png",520,750)
image buller2 = im.Scale("buller2.png",520,750)
image thunhoibong = im.Scale("thunhoibong.png",420,320)
image tintuc = im.Scale("tintuc.png",1920,1080)
image tintuc2 = im.Scale("tintuc2.png",1920,1080)
define luxury = Character("Luxury",color="#C7E80E", image="luxury")
define m = Character("Mẹ Harime", color="#6B2BB0")


# The game starts here.

label start:
    play music "/images/nhacnen.ogg" volume 0.3
    call variables from _call_variables
    "Vào một buổi sáng nọ..."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene duongpho

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show side qa1:
        xpos 550 ypos 200
    with dissolve
    # These display lines of dialogue.
label sprites:
    $ playername = renpy.input("Vui lòng nhập tên")
    $ playername = playername.strip()
    if not playername:
        $ playername = "Thông"
    e "Chào buổi sáng, [playername] ! "
    a "Chào cậu."
    e "Buổi sáng hôm nay đẹp thật ha"
    e "Hôm nay cậu cảm thấy như thế nào ?"
    a "Tớ ổn"
    e "Bữa nay tớ có rất nhiều thứ muốn kể với cậu đấy..."
    a "Oh! Vậy sao, tớ đang háo hức muốn nghe đấy"
    e "Chúng ta vừa đi vừa kể nhé"
scene black
pause 0.5
scene truonghoc
show side qa1:
        xpos 550 ypos 200
screen textadd:
    text"Điểm tình yêu: [lovescore]" yalign 1 xalign 0.97
show screen textadd
label nuoicho:
    e "Nhà tớ vừa nhận nuôi một chú chó đó"
    e "Có vẻ như nó muốn làm quen với cậu (cười khúc khích)"
    e "Cậu có muốn sang nhà tớ để chơi cùng nó không ?"
menu:
    "Cũng được, khi tan học tớ sẽ đi với cậu":
        jump case3

    "Thôi tớ không rảnh đâu":
        jump case4
    "..."
label case3:
    e "Thật sao ? Cậu hứa rồi đấy nhé" 
    a2 "Tất nhiên rồi"
    e "Vậy khi tan học hẹn cậu ở cổng trường"
    $ lovescore += 25
    "(Bạn nhận được 25 điểm tình yêu)"
    scene phongharime 
    hide qa
    jump quanha
label case4:
    e "Ừm không sao đâu, nhưng phải bữa khác đấy nhé"
    a2 "Oki, tớ biết rồi !!"
    "Vài hôm sau..."
    scene black
    pause 0.5
    scene phongharime
    hide qa
    if lovescore >= 10:
        jump quanha
    pass
label quanha:
    show side luxury at right
    pause 0.5
    show side luxury:
        xpos 1700 ypos 750
    with ease
    luxury "Gâu gâuuu..."
    e2 "Thôi nào, đừng làm cậu ấy ghét mày chứ"
    e2 "Tên nó là Luxury"
    a2 "Tên đẹp đấy, ngoan nào cún con"
    "(chơi với con chó)"
    e2 "Nhà tớ vừa nhận nuôi nó vào ngày hôm qua"
    e2 "Có người thấy nó bị bỏ rơi ở gốc cây, họ không muốn nhận nuôi nó vì sợ phiền phức"
    e2 "Nên nhà tớ mới xin về nuôi, nhìn bộ lông vàng ánh của nó nên tớ đã đặt tên như vậy đấy (cười khúc khích)"
    e2 "Có nó lúc bầu bạn khi ở một mình tớ cảm thấy khá dễ chịu hơn trước"
    e2 "Và cả cậu nữa..."
    a "Tớ sao ?"
    e2 "[a] này, tớ có chuyện muốn nói với cậu..."
    e4 "Tớ nghĩ là tớ... (ấp úng)"
menu:
    "Lắng nghe":
        jump langnghe
    "Phớt lờ":
        jump photlo
label langnghe:        
        a "Có chuyện gì sao ?"
        e2 "Tớ nghĩ có điều gì đó đặc biệt đối với cậu"
        a "Vậy sao, có phải đó là một thứ gì đó khó nói lắm nhỉ ?"
        e2 "Tớ... (ngại ngùng)"
        m "(cốc cốc) Harime ơi mẹ về rồi này"
        m "Có bạn qua chơi hả con, kêu bạn ấy xuống dùng bữa với mình luôn nhé"
        e4 "(giật mình) Vâ... vâng ạ"
        "(Bạn nhận được 25 điểm tình yêu)"
        $ lovescore += 25
        jump lophoc
label photlo:        
        e2 "À thôi không có gì đâu tớ nhầm tí"
        m "(cốc cốc) Harime ơi con và bạn xuống ăn cơm này"
        e2 "Vâng ạ, thôi mình xuống ăn cơm nhé"
        "Oke"
label lophoc:
        scene black
        pause 0.5         
        scene hanhlang
        hide qa
        show buller1
        show buller at left:
            xpos 150
        show buller2 at right:
            xpos 1600
        stop music fadeout 1.0
        play music "/images/nhachanhdong.ogg" volume 0.3
        b "Ê con kia, mày đứng lại cho tao !!"
        e2 "Có chuyện gì vậy ạ ?"
        b "Mày đừng có giả nai, chuyện mày làm với bọn tao... "        
        b "Đi lên sân thượng ngay lập tức !!"
label santhuong:
        scene black
        pause 0.5
        scene santhuong1
        with pushup
        show buller1
        show buller at left:
            xpos 150
        show buller2 at right:
            xpos 1600
        b "Mày là đứa đã ăn cắp đồ của bọn tao đúng không ?"         
        b "Tụi bây... lục soát người nó"         
        b "Vâng đại ca"
        hide buller
        hide buller1
        hide buller2
        show side qa 
        with hpunch
        e "Áaaa"
        hide side qa
        show thunhoibong:
            xpos 750 ypos 450
        with dissolve
        b "Cái này là cái gì đây ?"
        b "Chẳng phải đây là con gấu bông yêu thích của tao sao ?"
        e2 "T..tớ chỉ..."
        hide thunhoibong
        with dissolve
        show buller1
        show buller at left:
            xpos 150
        show buller2 at right:
            xpos 1600
        b "Hôm nay là ngày tàn của mày rồi, dám lấy đồ của tao ư"
        e2 "Th..tha cho tớ"
        e2 "Tớ không có ý đó, tớ chỉ định nhặt lại và trả cho cậu thôi"
        e2 "Lúc ra về cậu bỏ quên trên bàn học, hôm ấy tớ ở lại trực nhật và thấy nó nên đã nhặt được"
        e2 "Nên tớ không phải là kẻ ăn cắp"
        b "Ý của mày là do tao ngu chứ gì ! Bây đâu cho nó nhừ xương"
label nghetrom:
        scene black
        pause 0.5
        scene hanhlang
        a "Sao trên đấy có chuyện gì ồn thế nhỉ ?"
menu:
    "Đi lên và xem":
        jump dilenxem
    "Mặc kệ":
        jump macke
label dilenxem:
        scene black
        pause 0.5
        scene santhuong1
        with pushup
        a "Đấy không phải là Harime sao ?"
        a "DỪNG LẠIII"
        b "Á à thằng oắt con nào đây ? 'Anh hùng cứu mỹ nhân' à"
        b "Xin lỗi nhé bọn tao không có nhu cầu xem diễn kịch ở đây đâu"
        a "Harime đã nói là không phải ăn cắp của tụi bây rồi mà"
        a "Cậu ấy đã trả lại đồ cho tụi bây rồi mà vẫn còn muốn đánh người à ?"
        b "Nói nhiều quá, ăn cắp là ăn cắp"
        b "Xử luôn thằng này cho tao !!"
        
        a "LÊN HẾT MỘT LƯỢT ĐI !!"

        a "Arggghhhh!!!!!!" with vpunch
        b "Má nó ! Đụng nhầm 'hàng khủng' rồi"
        b "Rút thôi tụi bây !!"
        show buller1
        show buller at left:
            xpos 150
        show buller2 at right:
            xpos 1600
        pause 0.5
        hide buller
        with dissolve
        hide buller1
        with dissolve
        hide buller2
        with dissolve
        a "Cút xéo hết đi"
        "(Chạy đến Harime)"
        stop music fadeout 1.0
        play music "/images/nhactinhcam.ogg" volume 0.3
        a "Cậu có sao không ?"
        show side qa1
        e "Tớ không sao, cảm ơn cậu nhiều lắm"
        e "Nếu không có cậu tớ không biết mình sẽ bị như thế nào nữa"
        a "Không có gì, cậu không sao là ổn rồi"
        a "Thật ra có phải là cậu đã..."
        e "Ừm là tớ đã lấy con gấu bông đấy"
        e "Tớ xấu xa đáng ghét lắm cậu đừng làm bạn với tớ nữa..."
        e "Từ trước đến giờ chẳng có ai muốn kết bạn với tớ cả...(hức hức)"
        a "Là để tặng cho tớ đúng không ?"
        e "(gật gù) sao cậu biết...??" 
        a "Tớ thấy hết rồi"
        "Chiều hôm ấy..."
label lophocchieu:
    pause 0.5
    scene lophocchieu
    with pixellate
    e2 "Con gấu đó dễ thương quá, là của ai vậy nhỉ ?"
    show thunhoibong:
        xpos 1050 ypos 450
    e2 "A mình nhớ rồi, đây là đồ chơi của con ả chuyên bắt nạt người khác đây mà"
    e2 "Nếu vậy thì mình sẽ giữ nó"
    e2 "Hay là tặng cho cậu ấy nhỉ ?"
    e2 "Quyết định rồi... chắc cậu ấy sẽ vui lắm đây (cười khúc khích)"
label dilenxem2:
    scene santhuong1
    with pixellate
    show side qa1
    e "Thì ra cậu đã biết hết rồi sao..."
    e "Liệu tớ có còn xứng đáng được làm bạn với cậu nữa không ?"
    a "Tất nhiên rồi, chúng ta vẫn là bạn như trước đây thôi"
    a "Thôi đứng dậy nào ! Để tớ dìu cậu vào phòng y tế nhé"
    e "Cảm ơn cậu"
    "(Bạn nhận được 50 điểm tình yêu)"
    $ lovescore += 50
    jump disinhnhat
label macke:
    a "Harime đâu rồi nhỉ ?"
    a "Chắc có lẽ cậu ấy đang đi toilet thôi "
    a "Thôi thì mình về lớp đợi vậy..."
    stop music fadeout 1.0
    pause 0.5
    scene lophocsang
    with pushleft
    queue music "/images/nhacnen.ogg"
    a "Ô cậu đi đâu nãy giờ thế, tớ tìm cậu mãi"
    a "Cậu ở đây từ lúc nào đấy ?"
    e2 "Tớ vừa đi toilet ấy mà và giải quyết một số rắc rối"
    a "Cậu có chuyện gì à ? Tớ chả nghe cậu kể gì"
    e2 "À không có gì đâu, cũng chẳng đáng để mình bận tâm đâu"
    a "Hmmm... có gì thì phải nói với tớ đấy nhé"
    e2 "Tớ biết rồi, à ngày mai là tới ngày sinh nhật của tớ đấy"
    a "Vậy sao ? Thật bất ngờ quá tớ chưa chuẩn bị quà gì cả..."
    e2 "Tớ không cần quà, tớ chỉ muốn cậu đi chơi với tớ khi tan học thôi được chứ ?"
    a "Được rồi tớ sẽ đến đúng giờ"
label thoisu:
    pause 1.0
    show tintuc
    pause 2.0
    show tintuc2
    a "..."    
    a "Ủa là trường mình đây mà ? Nghe có vẻ rất nguy hiểm"
    a "Đáng sợ thật, không biết thực hư như thế nào"
    a "Ngày mai mình sẽ hỏi Harime vậy"
    scene black
    "(Sáng hôm sau...)"
    scene duongpho
    a "Hôm qua tớ coi thời sự trên TV đưa tin đáng sợ thật"
    a "Cậu có biết gì về sự việc ấy không ?"
    e2 "Tớ không biết..."
    e2 "Nhưng nghe nói nạn nhân là mấy đứa hay bắt nạt người khác, đáng đời lắm"
    a "Ừm hi vọng nhà trường sẽ chấm dứt được tình trạng bạo lực học đường"
    a "Tớ cảm thấy trường học cũng không phải là nơi an toàn"
    "(Cả hai im lặng một lúc)"
    e2 "À tối nay tớ đợi cậu ở trạm xe buýt nhé (háo hức)"
    e2 "Thôi mình đi học nhanh đi kẻo trễ giờ đấy"  
label dilehoi:
    scene lophocchieu
    "(Reng reng...)"
    label disinhnhat:
    scene lophocchieu
    with pushup
    "(Reng reng...)"
    e2 "Haizz cuối cùng cũng được về nhà"
    e2 "[a] này, tớ về trước nhé hẹn cậu sau"
    a "Oke ! Cậu về cẩn thận đấy"
    scene black
    pause 0.5
    scene tramxebuyt
    a "Tớ đến rồi này, cậu đợi có lâu không ?"
    e2 "Tớ vừa mới đến, cậu xuất hiện là tớ vui rồi"
    a "Woahh !! Cậu ăn mặc khác với lúc đi học thật đấy"
    e3 "Này !! Cậu đang khen hay chê tớ đấy ? (tức giận)"
    a "Tớ đùa thôi mà, trông cậu xinh lắm đấy nên tớ có hơi bất ngờ"
    e3 "Ngay từ đầu không nói vậy đi"
    a "Hehe, đi thôi nào !"

    scene black
    screen textmiddle:
        text"(Cả hai đi chơi rất vui vẻ)" xalign 0.5 yalign 0.5
    show screen textmiddle
    pause 1.5
    hide screen textmiddle
    scene khuvuichoi
    stop music fadeout 1.0
    e2 "Hôm nay cậu cảm thấy như thế nào ?"
    a "Tớ vui lắm !!"
    a "Rất lâu rồi tớ không được đi đây đó, cả ngày chỉ đi học về rồi lại nằm ườn trên giường..."
    e2 "Nghe nhàm chán thật đấy, cậu có muốn luôn luôn được vui vẻ như thế này không ?"
    a "Tớ cũng muốn lắm, nhưng tớ phải có trách nhiệm với tương lai của chính mình"
    a "Nếu như ngày hôm nay không cố gắng thì sau này khó có thể vui vẻ được"
    e2 "Ừm tớ hiểu mà !! Ý của tớ muốn mình là người đem niềm vui đến cho cậu"
    e2 "Trước giờ tớ chỉ có một người bạn duy nhất đó là cậu"
    e2 "Cậu vẫn muốn chơi với tớ mặc cho người khác họ buông những lời dè bỉu với tớ"
    e2 "Tớ cảm thấy cậu thật đặc biệt so với mọi người"
    a "À những chuyện ngu ngốc như vậy tớ chả để tâm đâu"
    a "Cậu chẳng làm gì có lỗi hết, họ không thích cậu chẳng qua là cậu khác biệt và nó chẳng ảnh hưởng gì đến họ"  
    e2 "Vì vậy tớ...(ấp úng)"
menu:
    "Tớ cũng thích cậu":
        jump chapnhan
    "Tớ nghĩ chúng ta nên thích hợp làm bạn thì hơn":
        jump tuchoi
label chapnhan:
    play music '/images/Death.ogg' volume 0.3
    scene black
    screen textmiddle2:
        text"(Cả hai trao nhau nụ hôn...)" xalign 0.5 yalign 0.5
    show screen textmiddle2
    pause 1.5
    hide screen textmiddle2
    return
label tuchoi:
    scene khuvuichoi
    play music '/images/Death.ogg' volume 0.3
    e2 "Cậ...cậu không thích tớ thật sao..."
    e2 "Tớ nghĩ sau những chuyện cả 2 đã trải qua cùng nhau, mình đã..."
    e2 "Thì ra cậu cũng giống như bọn họ, cậu cũng ghét tớ"
    a "Đó chỉ là cậu nghĩ như vậy thôi, tớ không ghét cậu"
    a "Cậu chẳng làm gì sai cả, nhưng với tớ hiện tại không phải là lúc để nói đến chuyện tình cảm"
    a "Vẫn cứ là bạn bè đi... như vậy sẽ tốt hơn"
    e2 "Ừm tớ hiểu rồi !!"
    e2 "Thôi tớ về trước nhé, hôm nay vui lắm..." 
    e2 "Cảm ơn cậu vì ngày hôm nay đã dành thời gian cho tớ"
    a "Cảm ơn và tạm biệt... !!"
    scene black
    "(Về đến nhà...)"
    screen lamphep:
        text"Harime đang làm những nghi thức kì lạ và lẩm bẩm gì đó..." xalign 0.5 yalign 0.5
    show screen lamphep
    with dissolve
    pause 1.0
    e "Cậu không giống họ"
    e "Tớ yêu cậu, [a]"
    e "Cậu sẽ mãi là của tớ... mãi bên tớ..."
    e "Mãi mãi..."
    hide screen lamphep
    with dissolve
    show thunhoibong:
        xpos 750 ypos 450
    with dissolve
    pause 0.5
    hide thunhoibong
    with dissolve
    show side tui
    with dissolve
    pause 0.5
    hide side tui
    with dissolve
    show thunhoibong:
        xpos 750 ypos 450
    with dissolve
    pause 0.5
    hide thunhoibong
    with dissolve
    show side tui
    with dissolve
    pause 0.5
    hide side tui
    with dissolve
    show thunhoibong:
        xpos 750 ypos 450
    with moveinleft
    pause 0.5
    show side tui at center
    with moveinright
    hide thunhoibong
    with dissolve
    hide side tui
    with dissolve
    show thunhoibong:
        xpos 750 ypos 450
    with dissolve
    hide thunhoibong with dissolve
    pause 1.5
    screen endtext:
        text"(Kể từ đó Harime được bên nhau với [a] mãi mãi... )" xalign 0.5 yalign 0.5
    show screen endtext with dissolve
    pause 1.5
    hide screen endtext with dissolve
    screen endtext2:
        text"(Nhưng còn [a] không phải với hình hài là một con người... )" xalign 0.5 yalign 0.5
    show screen endtext2 with dissolve
    pause 1.5
    hide screen endtext2 with dissolve
    screen endtext3:
        text"The End" xalign 0.5 yalign 0.5
    show screen endtext3 with dissolve
    hide screen endtext3 with dissolve
label variables:
    $ lovescore = 0
    return