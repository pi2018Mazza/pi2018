from errbot import BotPlugin, botcmd, re_botcmd

class Food(BotPlugin):
    """Mensagens de food"""


    
    @re_botcmd(pattern=r"^[Ss]tart.*$")
    def start(self, msg, match):

        yield """Você quer algo doce ou salgado?"""
        yield """Se você deseja algo salgado digite Salgado"""
        yield """Se você deseja algo doce digite Doce """
        yield """ E caso você esteja com sede digite Bebidas"""
        yield """Muito simples, não é mesmo?"""                                                                                                         
    
    @re_botcmd(pattern=r"^[Ss]algado.*$")
    def Salgado(self, msg, match):

        yield """ Por favor selecione uma das seguintes categorias:
\Massas
\Carnes
\Vegetarianas
\Veganas Salgadas
\Saladas
\Risotos
\Farofas
\Aperitivos"""

     
    @re_botcmd(pattern=r"^[Dd]oce$")
    def Doce(self, msg, match):

        yield """ Por favor selecione uma das seguintes categorias:
\Veganas Doces
\Bolos
\Pudins
\Mousses
\Doces Festivos
\Tortas"""

    
    
    @re_botcmd(pattern=r"^[Bb]ebidas.*$")
    def Bebidas(self, msg, match):
        yield """ Por favor selecione uma das seguintes categorias:
\Sucos
\Chás
\Milkshake"""


#######==========================================================================================================================================================================================================================================================================================================SUCOS==========================================================================================================#######
    
    @re_botcmd(pattern=r"^[Ss]ucos$")
    def Sucos(self, msg, match):
        yield""" Eii, falta pouquinho... só falta escolher uma dessas receitas XD
\Suco verde tradicional 
\Suco de couve com maçã
\Suco verde de abacaxi e pepino
\Suco de laranja com acerola
\Limonada de morango
\Suco de uva com kiwi e hortelã"""

    
    
       
    @re_botcmd(pattern=r"^[Ss]uco [Vv]erde [Tt]radicional.*$")
    def Sucoverdetradicional(self, msg, match):
        self.send_stream_request(msg.frm, open('sucoverdetradicional.jpg', 'rb'), name='sucoverdetradicional.jpg', stream_type='photo')
        yield """Ingredientes
2 laranjas
3 folhas de couve 
1 pedacinho de gengibre 
1 litro de água."""

        yield """
Modo de preparo"""

        yield"""
Descasque as laranjas, corte-as em pedaços, tirando as sementes; coloque no liquidificador junto com as folhas de couve bem lavadas e com talo. 
Acrescente o gengibre e a água. Bata tudo. 
Coe só se necessário."""

    
    
    
    @re_botcmd(pattern=r"^[Ss]uco de [Cc]ouve com [Mm]a.*$")
    def Sucodecouvecommaca(self, msg, match):
        self.send_stream_request(msg.frm, open('sucoverdecommaca.jpg', 'rb'), name='sucoverdecommaca.jpg', stream_type='photo')
        yield """Ingredientes
2 maçãs 
2 folhas de couve 
½ limão 
200 ml de água."""

        yield"""
Modo de preparo
Corte as maçãs ao meio e retire suas sementes, colocando no liquidificador com os demais ingredientes.
Coe só se necessário."""


         
    @re_botcmd(pattern=r"^[Ss]uco [Vv]erde de [Aa]bacaxi e [Pp]epino.*$")
    def Sucoverdedeabacaxiepepino(self, msg, match):
        self.send_stream_request(msg.frm, open('sucoabacaxi.jpg', 'rb'), name='sucoabacaxi.jpg', stream_type='photo')
        yield """Ingredientes    
1 fatia média de abacaxi    
1 folha grande de couve
1 pedaço pequeno de pepino 
1 fatia fina de gengibre 
200 ml de água de coco (ou água)."""

        yield"""      
Modo de preparo"""
        yield"""
 Coloque todos os itens no liquidificador e depois bata bem para não precisar coar."""


          
    @re_botcmd(pattern=r"^[Ss]uco de [Ll]aranja com [Aa]cerola.*$")
    def Sucodelaranjacomacerola(self, msg, match):
        self.send_stream_request(msg.frm, open('sucolaranja.jpg', 'rb'), name='sucolaranja.jpg', stream_type='photo')
        yield """ Ingredientes
1 copo de suco de laranja
10 acerolas
2 cubos de gelo opcional"""

        yield"""    
Modo de preparo"""
        yield"""
Bata os ingredientes no liquidificador ou mixer e beba a seguir."""


    @re_botcmd(pattern=r"^[Ll]imonada de [Mm]orango.*$")
    def Limonadademorango(self, msg, match):
        self.send_stream_request(msg.frm, open('sucomorango.jpg', 'rb'), name='sucomorango.jpg', stream_type='photo')
        yield """Ingredientes
1 copo de água
Suco de 2 limões
5 morangos
2 cubos de gelo *opcional*"""
 
        yield """
Modo de preparo"""
        yield """
Bater os ingredientes no liquidificador ou mixer e beber a seguir."""




    
    @re_botcmd(pattern=r"^[Ss]uco de [Uu]va com [Kk]iwi e [Hh]ortel.*$")
    def Sucodeuvacomkiwiehortela(self, msg, match):
        self.send_stream_request(msg.frm, open('sucouva.jpg', 'rb'), name='sucouva.jpg', stream_type='photo')
        yield """Ingredientes
1 copo de suco de uva integral
1 kiwi picado
folhas de hortelã a gosto."""
        yield"""
Modo de preparo"""
        yield"""
Bata tudo no liquidificador."""

    





######========================================================================================CHÀS============================================================================================================================================================================================================================================================================================================================########
    
    @re_botcmd(pattern=r"^[Cc]h.s$")
    def Chas(self, msg, match):
        yield """ Eii, falta pouquinho... só falta escolher uma dessas receitas XD
\Chá de Capim Santo e Limão
\Chá indiano
\Chá com maçãs
\Chá de gengibre"""



    @re_botcmd(pattern=r"^[Cc]h.* de [Cc]apim [Ss]anto e [Ll]im.*o$")
    def Chadecapimsantoelimao(self, msg, match):    
        self.send_stream_request(msg.frm, open('chacapim.jpg', 'rb'), name='chacapim.jpg', stream_type='photo')
        yield """Ingredientes
300 ml de água;
1 folha de capim santo picada com tesoura;
1 gengibre sem casca e cortado em 4 pedaços de 0,5 cm;
1 rodela de centro de limão siciliano com casca."""

        yield"""    
Modo de preparo"""
        yield """
Ferva a água e depois acrescente os seguintes itens: capim santo, gengibre cortado e limão siciliano. 
Desligue o fogo e tampe por, aproximadamente, 5 minutos. 
Coe e sirva."""

        
    @re_botcmd(pattern=r"^[Cc]h.* [Ii]ndiano$")
    def chaindiano(self, msg, match):
        self.send_stream_request(msg.frm, open('chaindiano.jpg', 'rb'), name='chaindiano.jpg', stream_type='photo')
        yield """ Ingredientes
1/2 litro de água mineral
3 bagas de cardamomo
2 paus de canela
2 cravos da índia
3 cm de gengibre cortado em rodela
1 colher de sopa de mel ou calda de Agave
100 ml de leite de arroz sabor
Folhas de hortelã."""
        yield"""
Modo de preparo"""
        yield"""
Inicialmente, coloque todos os ingredientes para ferver em uma panela por 5 minutos, exceto o leite de arroz. 
Adicione-o por último e depois é só coar e saborear."""


    @re_botcmd(pattern=r"^[Cc]h.* com [Mm]a.*$")
    def chacommacas(self, msg, match):
        self.send_stream_request(msg.frm, open('chamaca.jpg', 'rb'), name='chamaca.jpg', stream_type='photo')
        yield """Ingredientes
1 L de água
2 pedaços de canela em pau
4 cravos
1 maçã pequena descascada em pedaços
2 saquinhos de chá mate"""
        yield"""
Modo de preparo"""
        yield """
Coloque para ferver a água com canela, o cravo e a maçã.
Depois adicione o mate, desligue o fogo e abafe por alguns minutos."""
        
    @re_botcmd(pattern=r"^[Cc]h.* de [Gg]engibre$")
    def chadegengibre(self, msg, match):
        self.send_stream_request(msg.frm, open('chagen.jpg', 'rb'), name='chagen.jpg', stream_type='photo')
        yield """Ingredientes
1 L de água
2 colheres de gengibre picada
1 rodela de limão sem casca"""
        yield"""
Modo de preparo"""
        yield""" 
Ferva a água por, aproximadamente, 10 minutos e coloque o gengibre e o limão. 
Abafe, coe e sirva."""#####=========================================================================================================================================================================================================================================================================================================================================================================================================================########      
  


    @re_botcmd(pattern=r"^[Mm]ilkshakes$")
    def Milkshakes(self, msg, match):
        yield """ Eii, falta pouquinho... só falta escolher uma dessas receitas XD
\Milkshake de chocolate com chantilly
\Milkshake de Ovomaltine
\Milkshake de banana
\Milkshake de cappuccino
\Milkshake de morango
\Milkshake de pêssego
\Milkshake de mirtilos"""



    @re_botcmd(pattern=r"^[Mm]ilkshake de [Cc]hocolate com [Cc]hantilly$")
    def Milkshakedechocolatecomchantilly(self, msg, match):
        self.send_stream_request(msg.frm, open('milkchant.jpg', 'rb'), name='milkchant.jpg', stream_type='photo')
        yield """Ingredientes
4 bolas de sorvete de chocolate
2 xícaras de leite"""
        yield """
Chantilly caseiro"""
        yield """
1 lata de creme de leite sem soro
3 colheres de sopa de açúcar
100g de manteiga
½ colher de sobremesa de essência de baunilha
1 colher de sobremesa de fermento em pó"""
        yield """
Modo de preparo"""
        yield """
Coloque no liquidificador o sorvete e o leite, bata bem. 
Se a mistura ficar muito grossa acrescente mais leite. 
Forre a taça com a calda de sorvete e coloque o milk-shake. """
        yield """
Chantilly caseiro"""
        yield """
Coloque  na batedeira, o creme de leite e o açúcar, bata até a massa ficar fofinha. Acrescente a manteiga, a baunilha e o fermento em pó. 
Bata até ficar com uma consistência de creme. 
Coloque o chantili por cima do milk shake. 
Está pronto para servir."""

   
    @re_botcmd(pattern=r"^[Mm]ilkshake de [Oo]vomaltine.*$")
    def Milkshakedeovomaltine(self, msg, match):
        self.send_stream_request(msg.frm, open('milkovo.jpg', 'rb'), name='milkovo.jpg', stream_type='photo')

        yield """Ingredientes
100 ml de leite integral
3 bolas de sorvete de creme
4 colheres de sopa de Ovomaltine."""

        yield"""
Modo de preparo"""
       
        yield""" 
Misture o sorvete de creme com o leite no liquidificador e bata bem, até que fique pastoso. Misture o Ovomaltine com o milkshake batido, com ajuda de uma colher, até que a mistura fique uniforme. 
Finalize decorando o copo com calda de chocolate e sirva imediatamente."""

    @re_botcmd(pattern=r"^[Mm]ilkshake de [Bb]anana.*$")
    def Milkshakedebanana(self, msg, match):
        self.send_stream_request(msg.frm, open('milkbanan.jpg', 'rb'), name='milkbanan.jpg', stream_type='photo')
        yield """Ingredientes
2 bananas descascadas
200ml de leite fresco
1 colher de mel ou uma bola de sorvete de baunilha (opcional)"""
        yield """
Modo de preparo"""
        yield """
Descasque as bananas e corte-as pela metade. 
Coloque num liquidificador o leite e depois as bananas. 
Processe primeiro na velocidade baixa e depois que perceber que a banana começa a ficar mais suave, aumente a velocidade aos poucos.
Você irá perceber que o milk shake está no ponto quando a mistura de leite e banana correr suavemente no liquidificador. 
Desligue-o e adicione o mel ou o sorvete de baunilha e liquidifique novamente."""

    @re_botcmd(pattern=r"^[Mm]ilkshake de [cc]appuccino.*$")
    def Milkshakedecappuccino(self, msg, match):
        self.send_stream_request(msg.frm, open('milkcap.jpg', 'rb'), name='milkcap.jpg', stream_type='photo')

        yield """ Ingredientes
1 e ½ xícara de chá de leite gelado
1 colher de sopa de café solúvel
3 bolas de sorvete sabor chocolate
Chocolate em pó ou raspas de chocolate para decorar
Cobertura para sorvete sabor chocolate para decorar"""
        yield """
Modo de Preparo"""
        yield """
Bata no liquidificador o leite gelado, o sorvete e o café solúvel até obter uma mistura homogênea. 
Distribua nos copos, polvilhe com o chocolate em pó ou com as raspas de chocolate. 
Sirva em seguida bem gelado."""

   
    @re_botcmd(pattern=r"^[Mm]ilkshake de [Pp].*ssegos.*$")
    def Milkshakedepessego(self, msg, match):
        self.send_stream_request(msg.frm, open('milkpes.jpg', 'rb'), name='milkpes.jpg', stream_type='photo')

        yield """Ingredientes
2 colheres de sopa de calda ou cobertura de morango
1 xícara de chá de leite gelado
2 colheres de sopa de geleia de morango
½ xícara de chá de sorvete de morango"""
        yield """
Modo de preparo"""
        yield """
Espalhe a calda ou cobertura de morango no interior de um copo alto e reserve. 
No copo do liquidificador, coloque o leite, a geleia e o sorvete de morango. 
Bata por 2 minutos ou mais, até ficar com bastante espuma. 
Passe para o copo com a calda e sirva em seguida."""
        yield """ Ingredientes
1 caixinha de creme de leite
3 copos de leite desnatado
½ xícara de chá de sorvete de creme
2 colheres de sopa de açúcar
2 pêssegos"""
        yield """
 Modo de Preparo"""
        yield """
No liquidificador, bata o leite e os pêssegos. 
Acrescente o creme de leite e continue a bater. 
Adicione os ingredientes restantes e bata mais um pouquinho. 
Sirva bem gelado."""

    @re_botcmd(pattern=r"^[Mm]ilkshake de [Mm]irtilos.*$")
    def Milkshakedemirtilos(self, msg, match):
        self.send_stream_request(msg.frm, open('milkmir.jpg', 'rb'), name='milkmir.jpg', stream_type='photo')

        yield"""Ingredientes
300g de mirtilos
100g de framboesas
100 ml de leite
2 colheres de sopa de açúcar"""
        yield """ 
Modo de Preparo"""
        yield """
Bata todos os ingredientes no liquidificador.
Sirva gelado decorado com alguns mirtilos."""







#-----------------------------------------------------------------------------MASSAS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#   
    
    @re_botcmd(pattern=r"^[Mm]assas.*$")
    def Massas(self, msg, match):
        yield """ Ok, estamos quase lá... escolha um dos pratos principais: +
\Lasanha
\Pizza
\Pastel
\Panquecas"""       
   
########                                                             #-----PIZZA------#                                                   ########
   
    
    @re_botcmd(pattern=r"^[Pp]izza$")
    def Pizza(self, msg, match):
        yield """ Eii, falta pouquinho… só falta escolher uma dessas receitas XD 
\Pizza de calabresa
\Pizza de frango
\Pizza de chocolate"""


  
    
    @re_botcmd(pattern=r"^[Pp]izza de [Cc]alabresa.*$")
    def Pizza_de_calabresa(self, msg, match):
        self.send_stream_request(msg.frm, open('pizzacala.jpg', 'rb'), name='pizzacala.jpg', stream_type='photo')

        yield """Ingredientes
Massa

500 g de farinha de trigo
25 g de fermento para pão
1 copo de água
1 ovo
50 g de gordura
1 colher de sopa de fermento em pó
1 colher de café de sal"""
        

        yield """
Molho

300 g de tomate maduro
50 g de queijo parmesão ralado
Sal
Orégano
1 colher de sopa de azeite de oliva"""
        
        yield """
Cobertura

300 g de linguiça calabresa defumada
Sem casca e em rodelas finas
2 cebolas em rodelas finas
1/2 xícara de chá azeitona preta sem caroço
1 colher de sopa de azeite de oliva
1 colher de café de orégano """
        
        yield """
Modo de preparo"""


        yield """
Molho
Bata o tomate no liquidificador com os demais ingredientes até formar uma mistura homogênea
Massa
Misture 50 g de farinha, fermento e um pouco de água
Deixe descansar por 20 minutos
Adicione os demais ingredientes e amasse até obter uma massa bem macia
Corte em 3 partes iguais, forme 3 bolas e cubra-as com um pano
Deixe descansar por 1 hora
Abra a massa com um rolo até obter 25 cm de diâmetro
Espalhe o molho de tomate por cima e leve para assar em forno pré-aquecido, a 180ºC, por 15 minutos
Retire e deixe esfriar """
        
        yield """
Cobertura

Espalhe a linguiça sobre o molho de tomate e cubra com a cebola
Decore com a azeitona e regue com azeite e orégano
Retorne ao forno por mais 10 minutos
Retire do forno e sirva imediatamente"""


    
    @re_botcmd(pattern=r"^[Pp]izza de [Ff]rango.*$")
    def Pizza_de_frango(self, msg, match):
        self.send_stream_request(msg.frm, open('pizzafrango.jpg', 'rb'), name='pizzafrango.jpg', stream_type='photo')

        yield """Ingredientes
Cobertura

1 peito pequeno de frango
1 sache de molho de tomate para pizzas
1 tomate em rodelas
1 cebola em rodelas
1 ovo em rodelas
Fatias de queijo mussarela
Orégano"""
        

        yield """
Modo de preparo

Cozinhe o frango com os temperos que desejar e desfie
Depois de assada a massa, despeje bastante molho de tomate sobre ela
A seguir espalhe o frango desfiado
Cubra o frango com as fatias de queijo, não economize no queijo, quanto mais melhor
A seguir distribua algumas rodelas de ovo, tomate e cebola e salpique o orégano sobre a pizza
Leve novamente ao forno até derreter o queijo."""
  
  
    
    @re_botcmd(pattern=r"^[Pp]izza de [Cc]hocolate.*$")
    def Pizza_de_chocolate(self, msg, match):
        self.send_stream_request(msg.frm, open('pizzachoco.jpg', 'rb'), name='pizzachoco.jpg', stream_type='photo')

        yield """Ingredientes
Massa

1/2 kg de farinha
4 colheres de sopa de açúcar
1 colher de sobremesa de sal
2 ovos
1/2 pacotinho de fermento para pães
1 xícara de leite
1 xícara de óleo"""
        

        yield """
Cobertura
250 g de chocolate (de sua preferência)"""
        

        yield """
Modo de preparo"""

        yield """
Massa

Misture os ingredientes secos em um recipiente
Coloque então o leite morno e o óleo e misture a massa até ficar homogênea e não grudar nos dedos
Amasse até dar liga
Abra e corte em forma de círculo
Unte uma assadeira e asse a massa, tire do forno antes que ela doure, pois tem que ficar assada mas branquinha"""

        yield """

Cobertura

Derreta o chocolate em banho-maria (não pode cair nenhuma gota de água no chocolate)
Depois que o chocolate derreter coloque na massa ainda quente
Salpique a castanha moída por cima e coloque para assar por 2 minutos para que o chocolate borbulhe."""

  




########                                                             #---------PANQUECA-------#                                                  ########
  
  
  
    
    @re_botcmd(pattern=r"^[Pp]anqueca.$")
    def Panqueca(self, msg, match):
        yield """ Eii, falta pouquinho… só falta escolher uma dessas receitas XD
\Massa de panqueca
\Panqueca de frango
\Panqueca de carne moída
\Panqueca doce"""


    
    @re_botcmd(pattern=r"^[Mm]assa de [Pp]anqueca.*$")
    def Massa_de_panqueca(self, msg, match):
        self.send_stream_request(msg.frm, open('massa.jpg', 'rb'), name='massa.jpg', stream_type='photo')

        yield """Ingredientes
2 xícaras (chá) de farinha de trigo
2 xícaras (chá) de leite
3 ovos
1 pitada de sal"""
         

        yield """

Modo de preparo

Bata todos os ingredientes no liquidificador por 2 minutos
Em seguida desligue e, com uma colher, misture a farinha que grudou no copo do liquidificador
Bata novamente só para misturar, reserve
Unte a frigideira com um fio de óleo e leve ao fogo até aquecer
Com o auxílio de uma concha, pegue uma porção de massa e coloque na frigideira, gire a frigideira para espalhar bem a massa
Abaixe o fogo e deixe dourar por baixo, em seguida vire do outro lado e deixe dourar, repita o processo com toda a massa."""


    
    @re_botcmd(pattern=r"^[Pp]anqueca de [Cc]arne [Mm]o.*$")
    def Panqueca_de_carne_moida(self, msg, match):
        self.send_stream_request(msg.frm, open('pcarne.jpg', 'rb'), name='pcarne.jpg', stream_type='photo')

        yield """Ingredientes
Massa

1 e 1/2 xícara (chá) de farinha de trigo
1 xícara (chá) de leite
2 ovos
4 colheres (sopa) de óleo
sal a gosto"""
        
        yield """

Recheio

300 g de carne moída
2 colheres (sopa) de cebola picada ou ralada
1/2 tomate cortado em cubos
1/2 lata de extrato de tomate
1 caixa de creme de leite
sal a gosto
400 g de mussarela fatiado
queijo ralado a gosto"""
        
        yield """

Modo de preparo"""

        yield """
  
Massa

Bata no liquidificador os ovos, o leite, o óleo, e acrescente a farinha de trigo aos poucos
Após acrescentar toda a farinha de trigo, adicione sal a gosto
Misture a massa até obter uma consistência cremosa
Com um papel toalha, espalhe óleo por toda a frigideira e despeje uma concha de massa
Faça movimentos circulares para que a massa se espalhe por toda a frigideira
Espere até a massa soltar do fundo e vire a massa para fritar do outro lado"""
        
        yield """

Recheio

Em uma panela, doure a cebola com o óleo e acrescente a carne
Deixe cozinhar até que saia água da carne, diminua o fogo e tampe
Acrescente o tomate picado e tampe novamente
Deixe cozinhar por mais 3 minutos e misture
Acrescente o extrato de tomate e temperos a gosto
Deixe cozinhar por mais 10 minutos
Quando o molho engrossar, desligue o fogo
Deixe esfriar o molho, acrescente o creme de leite e misture bem
Quando estiver bem homogêneo, leve novamente ao fogo e deixe cozinhar em fogo baixo por mais 5 minutos"""
        
        yield """

Montagem

Recheie a panqueca com uma fatia de mussarela, uma porção de carne e enrole
Faça esse processo com todas as panquecas
Despeje um pouco de caldo no fundo de um refratário, para untar
Disponha as panquecas já prontas no refratário e despeje sobre elas o restante do molho
Polvilhe queijo ralado sobre as panquecas
Leve ao forno para gratinar, em fogo médio, por 20 minutos ou até que o queijo esteja derretido.   """


    
    @re_botcmd(pattern=r"^[Pp]anqueca de [Ff]rango.*$")
    def Panqueca_de_frango(self, msg, match):
        self.send_stream_request(msg.frm, open('pfrango.jpg', 'rb'), name='pfrango.jpg', stream_type='photo')

        yield """Ingredientes
Massa

3 ovos
2 xícaras de chá de farinha de trigo
2 xícaras de chá de leite
2 colheres de sopa de manteiga
1 colher de chá de sal"""
        
        yield """

Recheio

2 peitos de frango sem osso
1 sachê de caldo de galinha
1 lata de molho de tomate pronto
2 colheres de sopa de azeite
1/2 cebola picada
3 dentes de alho amassados
pimenta, sal e salsinha a gosto"""
        
        yield """

Modo de preparo"""

        yield """

Massa

Bata no liquidificador todos os ingredientes durante 3 minutos, deixe descansando
Recheio
Cozinhe o peito de frango em um pouco de água com o caldo de galinha, até ficar bem cozido
Retire da panela em que foi cozido e comece a desfiar com um garfo
Leve uma panela ao fogo, coloque o azeite a cebola picada e o alho, deixe dourar
Acrescente o frango desfiado e tempere com pimenta e sal e mexa
Deixe refogar por 5 minutos mexendo de vez em quando, agora acrescente um pouco
de molho de tomate só para dar um corzinha no frango e retire do fogo e reserve
Agora faremos a panqueca, use uma frigideira teflon rasa unte-a com um pouco de manteiga
Coloque uma quantidade razoável de massa da frigideira que não fique grossa, vá fazendo até acabar a massa
Agora coloque um pouco de recheio na ponta da panqueca e enrole faça isso com todas, vá colocando todas em uma forma retangular para ir ao forno
Agora aqueça o molho de tomate e derrame em cima das panquecas jogue um pouco de queijo parmesão em cima se preferir e leve ao forno preaquecido por 5 minutos."""


    
    @re_botcmd(pattern=r"^[Pp]anqueca [Dd]oce.*$")
    def Panqueca_doce(self, msg, match):
        self.send_stream_request(msg.frm, open('pdoce.jpg', 'rb'), name='pdoce.jpg', stream_type='photo')

        yield """Ingredientes
Massa

1 ½ xícara (chá) de leite
1 xícara (chá) de farinha de trigo
1 colher (chá) de essência de baunilha
1 colher (chá) de óleo
1/3 xícara (chá) de chocolate em pó"""
        
        yield """

Recheio

1 lata de leite condensado
3 colheres (sopa) de chocolate em pó
1 colher de sopa de manteiga
1 caixinha de creme de leite"""
        

        yield """
Modo de preparo"""

        yield """
 
Massa

Bater todos os ingredientes no liquidificador
Fritar as massas em frigideira untada com margarina"""
       
        yield """

Recheio

Levar ao fogo o leite condensado, o chocolate em pó e a manteiga até que fique em ponto de brigadeiro
Desligar o fogo e misturar o creme de leite
Esperar esfriar e levar para gelar
Depois, rechear as panquecas.        """






########                                                             #---------PASTEL--------#                                                   ########

    
    @re_botcmd(pattern=r"^[Pp]astel.$")
    def Pastel(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD
\Massa de pastel
\Pastel romeu e julieta"""                      
    

    
    @re_botcmd(pattern=r"^[Mm]assa de [Pp]astel.*$")
    def Massa_de_pastel(self, msg, match):
        self.send_stream_request(msg.frm, open('massap.jpg', 'rb'), name='massap.jpg', stream_type='photo')

        yield """Ingredientes
3 xícaras de farinha de trigo
1 copo e meio de água (400 ml)
2 colheres (sopa) de óleo (opcional)
1 colher (sopa) de sal
1 dose de pinga (50 ml)"""
        

        yield """

Modo de preparo 

Misture bem a farinha com o sal.
Abra um buraco no meio da farinha e jogue, aos poucos, a água, incorporando-a à farinha com as mãos num bowl fundo ou numa mesa lisa. 
Se quiser dar uma liga a mais na massa, adicione as colheres de óleo.
Acrescente a cachaça e continue misturando bem a massa.Sove a massa, em uma superfície lisa, polvilhada de farinha, até que fique homogênea e pare de grudar nas mãos.
Deixe a massa descansar por 15 minutos coberta com pano úmido ou plástico filme.
Abra a massa com a ajuda de cilindros – é mais fácil – até a espessura mais fina que conseguir, sem que ela massa quebre; se não tiver a máquina, um rolo faz também a função.
Corte a massa já aberta com uma faca com até 30 cm de altura e 10 cm de largura, para ficar do tamanho de um pastel de feira.    
Recheie a massa, ocupando no máximo metade do espaço, dobre a massa e feche as bordas com a ajuda de um garfo.
Depois de montar os pastéis, leve o quanto antes ao óleo quente para fritar."""


    @re_botcmd(pattern=r"^[Pp]astel [Rr]omeu e [Jj]ulieta.*$")
    def Pastel_romeu_e_julieta(self, msg, match):
        self.send_stream_request(msg.frm, open('pastelromeu.jpg', 'rb'), name='pastelromeu.jpg', stream_type='photo')

        yield """Ingredientes
⅓ de xícara de farinha de trigo + ⅔ de farinha de trigo para colocar aos poucos
1 xícara de queijo muçarela
1 xícara de queijo parmesão ralado
2 ovos
100g de goiabada cascão em cubos
Gema para pincelar"""

        yield """
Modo de preparo

Dispor a farinha de trigo Dona Benta em uma tigela.
Juntar os queijos. 
Acrescentar os ovos e misturar.Adicionar o restante de farinha aos poucos e agregar até virar uma massa que não grude nas mãos.
Formatar as bolinhas, abrir com a ponta dos dedos em uma superfície enfarinhada.
Rechear com goiabada cascão. 
Fechar os pastéis.
Pincelar gema e levar ao forno preaquecido a 180 graus por 30 minutos ou até ficarem dourados."""

########                                                             #-------LASANHA------#                                                  ########

    
    @re_botcmd(pattern=r"^[Ll]asanha$")
    def Lasanha(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD
Lasanha de carne moída
Lasanha de frango
Lasanha de queijo com molho branco"""

    
    
    @re_botcmd(pattern=r"^[Ll]asanha de [Cc]arne [Mm]o.*$")
    def Lasanha_de_carne_moida(self, msg, match):
        self.send_stream_request(msg.frm, open('lasanhacarne.jpg', 'rb'), name='lasanhacarne.jpg', stream_type='photo')

        yield """Ingredientes
500 g de massa de lasanha
500 g de carne moída
2 caixas de creme de leite
3 colheres de manteiga
3 colheres de farinha de trigo
500 g de presunto
500 g de mussarela
sal a gosto
2 copos de leite
1 cebola ralada
3 colheres de óleo
1 caixa de molho de tomate
3 dentes de alho amassados
1 pacote de queijo ralado"""
        
        yield """

Modo de preparo"""
        yield """
Lasanha"""
        yield """
Cozinhe a massa segundo as orientações do fabricante, despeje em um refratário com água gelada para não grudar e reserve
Molho a bolonhesa
Refogue o alho, a cebola, a carne moída, o molho de tomate, deixe cozinhar por 3 minutos e reserve
Molho branco
Derreta a margarina, coloque as 3 colheres de farinha de trigo e mexa
Despeje o leite aos poucos e continue mexendo
Por último, coloque o creme de leite, mexa por 1 minuto e desligue o fogo"""
        
        yield """
Montagem"""
        yield """
Despeje uma parte do molho à bolonhesa em um refratário, a metade da massa, a metade do presunto, a metade da mussarela, todo o molho branco e o restante da massa
Repita as camadas até a borda do recipiente
Finalize com o queijo ralado e leve ao forno alto (220° C), preaquecido, por cerca de 20 minutos."""


    
    @re_botcmd(pattern=r"^[Ll]asanha de [Ff]rango.*$")
    def Lasanha_de_frango(self, msg, match):
        self.send_stream_request(msg.frm, open('lasanhafrango.jpg', 'rb'), name='lasanhafrango.jpg', stream_type='photo')

        yield """Ingredientes
1 peito de frango
500 g de queijo mussarela fatiado
400 g de presunto fatiado
1 pacote médio de massa para lasanha (direto ao forno, sem cozimento prévio)
1 pote de requeijão cremoso
2 caldos de galinha (ou tempero completo sabor galinha)
2 copos de leite
1 caixa de creme de leite
2 colheres de farinha
3 colheres de manteiga
1 cebola média"""
        
        yield """

Modo de preparo"""

        yield """

Molho"""
        yield """
Em uma panela, faça um creme homogêneo com as 2 colheres de farinha e 2 colheres de manteiga (reserve 1 colher de manteiga)
Acrescente o leite, 1 caldo de galinha e mexa constantemente
Retire do fogo e acrescente o creme de leite, reserve"""
        
        yield """

Frango"""
        yield """
Cozinhe o peito de frango em água (sem óleo), após cozido, desfie-o
Pique a cebola em pedaços pequenos, coloque em uma panela e doure com a manteiga
Acrescente o frango e o caldo de galinha, mexa sempre até o frango ficar totalmente dourado"""
        
        yield """

Montagem"""
        yield """
Em um refratário, coloque 2 conchas de molho
Faça a base com massa de lasanha, cubra com 1 camada de presunto, 1 de queijo e 1 de frango (nessa ordem)
Sobre o frango, coloque 1 camada de requeijão e 2 conchas de molho
Cubra o requeijão com 1 camada de presunto, 1 camada de queijo e 1 camada de massa, coloque molho
Repita esse processo até faltar cerca de 2,5 cm para chegar na borda do refratário
Para finalizar, cubra a lasanha com muito queijo, requeijão e molho
Asse por, aproximadamente, 20 minutos em fogo baixo."""


    
    @re_botcmd(pattern=r"^[Ll]asanha de [Qq]ueijo com [Mm]olho [Bb]ranco.*$")
    def Lasanha_de_queijo_com_molho_branco(self, msg, match):
        self.send_stream_request(msg.frm, open('lasanhaqueijo.jpg', 'rb'), name='lasanhaqueijo.jpg', stream_type='photo')

        yield """Ingredientes
1 pacote de lasanha
2 dentes de alho
Cebola a gosto
1 litro de leite
Sal a gosto
3 colheres de maisena
1 colher (sopa) bem cheia de manteiga
1 caixinha de creme de leite
Cheiro verde a gosto
Orégano a gosto"""
        
        yield """

Modo de preparo"""

        yield """

Molho"""
        yield """
Em um panela coloque a manteiga e frite o alho e a cebola
Em seguida acrescente o leite, a maisena e o sal
Mexa até formar um creme
Desligue o fogo e acrescente o cheiro verde e o creme de leite"""

        yield """

Montagem"""
        yield """
Em uma assadeira ou em um pirex faça uma camada de molho, em seguida coloque uma camada da massa da lasanha e em seguida coloque o queijo
Em cima do queijo jogue um pouco de orégano para dar um gostinho especial
Em seguida coloque molho novamente, outra camada de massa de lasanha e queijo e orégano novamente, faça mais uma camada (molho, massa, queijo) e por cima do queijo jogue um pouco mais de molho
Se preferir mais molhadinha jogue todo o molho restante, caso não prefira assim, jogue o molho até que cubra o queijo
Leve ao forno por 35 minutos aproximadamente."""

    
########                                                            #--------MACARRÃO-------#                                                  # ######
#=================================================================================Generico===========================================================
#    @re_botcmd(pattern=r"^[Xx]yyyy.*$")
#    def Xyyyy(self, msg, arg)
#         yield """sei la"""
#===============================================================================================================================================
    @re_botcmd(pattern=r"^[Mm]acarr.*$")
    def Macarrao(self, msg, match):
        yield """ tei """

   
   
   
   
   
   
   
   
#------------------------------------------------------------------------CARNES---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#-   
   
   
    
    @re_botcmd(pattern=r"^[Cc]arnes.*$")
    def Carnes(self, msg, match):
        yield """Ok, estamos quase lá… escolha um dos pratos principais:
\Frango
\Bovino
\Suino
\Peixe"""

  
########                                                             #-----FRANGO------#                                                   ########
    
    @re_botcmd(pattern=r"^[Ff]rango$")
    def Frango(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD
\Torta de frango
\Frango xadrez
\Filé de frango ao molho de iogurte
\Frango ao molho de laranja chinês"""

    
    @re_botcmd(pattern=r"^[Tt]orta de [Ff]rango.*$")
    def Torta_de_frango(self, msg, match):
        self.send_stream_request(msg.frm, open('tortafrango.jpg', 'rb'), name='tortafrango.jpg', stream_type='photo')

        yield """Ingredientes"""

        yield """
Massa""" 
        yield """
250 ml de leite
3/4 de xícara (chá) de óleo
2 ovos
1 e 1/2 xícara (chá) de farinha de trigo
sal a gosto
1 colher (sopa) de fermento em pó
queijo ralado a gosto"""
        
        yield """

Recheio"""
        yield """
500 g de peito de frango sem pele
1/2 litro de caldo de galinha
4 colheres (sopa) de óleo
1 dente de alho amassado
1 cebola picada
3 tomates sem pele e sem sementes
1 xícara (chá) de ervilhas
Sal e pimenta-do-reino a gosto"""
        
        yield """

Modo de preparo- recheio"""
        yield """
Cozinhe o peito de frango no caldo até ficar macio
Separe 1 xícara (chá) de caldo do cozimento e reserve
Refogue os demais ingredientes e acrescente as ervilhas por último
Desfie o frango, misture ao caldo e deixe cozinhar até secar """
        
        yield """
Modo de preparo- massa"""
        yield """
Bata o leite, o óleo e os ovos no liquidificador em velocidade baixa       
Acrescente aos poucos a farinha, o sal e o fermento
Despeje metade da massa em uma forma untada e adicione o recheio sobre ela
Cubra com o restante de massa e o queijo ralado
Leve ao forno preaquecido (180° C) até dourar."""


    
    @re_botcmd(pattern=r"^[Ff]rango [Xx]adrez")
    def Frango_xadrez(self, msg, match):
        self.send_stream_request(msg.frm, open('frangoxadrez.jpg', 'rb'), name='frangoxadrez.jpg', stream_type='photo')

        yield """
Ingredientes

1kg de frango em cubos
1 colher (sopa) de vinagre branco
1 pimentão vermelho em cubos
1 pimentão verde em cubos
1 pimentão amarelo em cubos
1 cebola em cubos
1 colher (sopa) de alho triturado
1 colher (chá) de gengibre em pó
sal e pimenta do reino a gosto
1 e 1/2 colher (sopa) de amido de milho
100ml de shoyu
1 xícara (chá) de água quente
1/2 xícara (chá) de amendoim torrado e sem pele (opcional)
Óleo vegetal
Para finalizar: 1 colher (sopa) de cebolinha verde"""

        yield """

Modo de preparo"""
        yield """
Tempere o frango em cubos com vinagre, sal (pouco sal) e pimenta do reino. Misture.
Na panela coloque um pouco de óleo, doure os cubos de frango. 
Acrescente a cebola em cubos, os pimentões em cubos, o alho triturado e o gengibre em pó. 
Misture bem, e deixe apurando alguns minutinhos.
Dissolva o amido de milho no shoyu e despeje no frango. 
Despeje também a água quente, e deixe apurando alguns minutos misturando de vez em quando até chegar no ponto.
Quando estiver pronto adicione o amendoim. 
Misture, desligue o fogo e 
finalize com cebolinha verde picada. """


    
    @re_botcmd(pattern=r"^[Ff]il.* de [Ff]rango ao [Mm]olho de [Ii]ogurte.*$")
    def File_de_frango_ao_molho_de_iogurte(self, msg, match):
        self.send_stream_request(msg.frm, open('filefrango.jpg', 'rb'), name='filefrango.jpg', stream_type='photo')

        yield """Ingredientes
2 filés de frango
2 dentes de alho triturados
suco de 1/2 limão
sal e pimenta do reino branca"""
        
        yield """

Molho de iogurte"""
        yield """
1 pote de iogurte (170g)
suco de 1/2 limão tahiti
suco de 1/2 limão siciliano
2 colheres (chá) de mostarda dijon
1 colher (chá) de mel
1 colher (chá) de azeite de oliva
1 colher (sopa) de manjericão picado (ou uma erva de sua preferência)
sal e pimenta do reino branca a gosto """
        
        yield """

Modo de preparo"""
        yield """
Tempere os filés de frango com suco de limão, alho, sal e pimenta do reino.
Em uma frigideira antiaderente doure os filés dos dois lados."""

        yield """
Para o molho de iogurte """
        yield """
Em uma tigela adicione todos os ingredientes do molho e misture bem.
Sirva a seguir os filés regados com o molho de iogurte."""


    
    @re_botcmd(pattern=r"^[Ff]rango ao [Mm]olho de [Ll]aranja [Cc]hin.*s")
    def Frango_ao_molho_de_laranja_chines(self, msg, match):
        self.send_stream_request(msg.frm, open('frangolaranja.jpg', 'rb'), name='frangolaranja.jpg', stream_type='photo')

        yield """Ingredientes
4 filés de peito de frango cortados em cubos
1 xícara de água gelada
1 ovo
1/2 colher (chá) de fermento em pó
1/2 colher (chá) de sal
2 xícaras de farinha de trigo
3 colheres (sopa) de gergelim torrado
sal e pimenta-do-reino
cebolinha para enfeitar
óleo para fritar"""
        
        yield """

Modo de preparo"""
        yield """
10 colheres (sopa) de suco de laranja
2 xícaras de água
1 xícara de açúcar
1/3 xícara vinagre de arroz
2 e 1/2 colheres (sopa) de molho shoyu
suco de 1 limão
1/2 colher (chá) de gengibre ralado
1/4 colher (chá) de alho ralado
4 colheres (sopa) de amido de milho
cebolinha picada a gosto
1 pimenta dedo-de-moça sem sementes picada."""


        








########                                                            #-----BOVINO------#                                                   ########
    
    @re_botcmd(pattern=r"^[Bb]ovino.*$")
    def Bovino(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD 
\Bife acebolado cremoso
\Bife ao alho
\Cupim
\Picanha grelhada
\Carne oriental """

    
    @re_botcmd(pattern=r"^[Bb]ife [Aa]cebolado [Cc]remoso.*$")
    def Bife_acebolado_cremoso(self, msg, match):
        self.send_stream_request(msg.frm, open('bifeacebolado.jpg', 'rb'), name='bifeacebolado.jpg', stream_type='photo')

        yield """Ingredientes
6 bifes de alcatra grossos
3 dentes de alho picados
Sal e pimenta-do-reino a gosto
8 colheres (sopa) de azeite
3 cebolas em rodelas
2 colheres (sopa) de molho inglês
6 colheres (sopa) de maionese"""
        
        yield """

Modo de preparo"""
        
        yield """
Tempere os bifes com o alho, sal e pimenta. 
Aqueça uma frigideira grande em fogo alto com metade do azeite e frite os bifes até dourarem dos dois lados. 
Retire e coloque em uma travessa. 
Volte a frigideira ao fogo médio com o azeite restante e frite a cebola até dourar. 
Misture o molho inglês, a maionese, espalhe sobre os bifes e sirva em seguida."""


    
    @re_botcmd(pattern=r"^[Bb]ife ao [Aa]lho.*$")
    def Bife_ao_alho(self, msg, match):
        self.send_stream_request(msg.frm, open('bifealho.jpg', 'rb'), name='bifealho.jpg', stream_type='photo')

        yield """Ingredientes
8 bifes de contrafilé
1 envelope de tempero em pó para carnes
Sal e pimenta-do-reino a gosto
2 colheres (sopa) de óleo
4 colheres (sopa) de manteiga
1 colher (sopa) rasa de açúcar
6 dentes de alho picados """
        
        yield """

Modo de preparo"""
        yield """
Tempere os bifes com o tempero em pó, sal e pimenta. 
Aqueça uma frigideira grande, em fogo alto, com o óleo e metade da manteiga, polvilhe com o açúcar e frite os bifes até dourarem dos dois lados. 
Retire e reserve em uma travessa. 
Volte a frigideira ao fogo baixo com a manteiga restante e frite o alho até dourar. 
Retire com uma escumadeira, espalhe sobre os bifes e sirva acompanhado de legumes cozidos, se desejar."""


    
    @re_botcmd(pattern=r"^[Cc]upim.*$")
    def Cupim(self, msg, match):
        self.send_stream_request(msg.frm, open('cupim.jpg', 'rb'), name='cupim.jpg', stream_type='photo')

        yield """Ingredientes
1 peça de Cupim (1kg)
1/2 xícara (chá) de molho de tomate
2 cebolas pequenas em cubinhos
4 dentes de alho triturados
sal e pimenta do reino a gosto
1 colher (sopa) de salsinha picada
1 colher (sopa) de cebolinha verde
1 folha de louro
1 colher (chá) de cominho em pó
1/2 colher (chá) de coentro em pó
Água quente, o suficiente"""
        
        yield """

Modo de preparo"""
        yield """
Corte o cupim em cubos médios.
Em uma panela regue um fio de azeite e doure os cubos de carne de todos os lados.
Tempere com sal, pimenta do reino, cominho e coentro em pó. 
Acrescente a cebola picada, o alho triturado, a cebolinha verde, o molho de tomate, e complete com água quente até cobrir a carne.
Tampe a panela, e deixe cozinhar por aproximadamente 2 horas, ou até que a carne esteja desmanchando.
No final salpique salsinha verde picada."""


    
    @re_botcmd(pattern=r"^[Pp]icanha [Gg]relhada.*$")
    def Picanha_grelhada(self, msg, match):
        self.send_stream_request(msg.frm, open('picanha.jpg', 'rb'), name='picanha.jpg', stream_type='photo')

        yield """Ingredientes
peça de picanha
sal grosso"""
                 
        yield """

Modo de tempero"""
        yield """
Com uma faca afiada, corte a picanha em medalhões.
Esmague um pouco o sal grosso, para que os pedacinhos de sal fiquem um pouco menores. Tempere cada medalhão com o sal dos dois lados.
Disponha os medalhões em uma grelha QUENTE. 
Deixe dourar de um lado, e quando começar a encorpar e dourar, vire para dourar do outro lado, sempre utilizando um pegador e nunca um garfo, para nãofurar a carne e deixar o suco sair.
         """


    
    @re_botcmd(pattern=r"^[Cc]arne [Oo]riental.*$")
    def Carne_oriental(self, msg, match):
        self.send_stream_request(msg.frm, open('coriental.jpg', 'rb'), name='coriental.jpg', stream_type='photo')

        yield """Ingredientes
400g de carne bovina 
Fio de Azeite
1 cebola cortada em tiras
2 dentes de alho triturados
½ xícara (chá) de castanha de caju
1 xícara (chá) de couve chinesa em tiras
1 xícara (chá) de brócolis cozido
4 colheres (sopa) de shoyu
1 colher (café) de curry
1 colher (sobremesa) de cebolinha verde picada
Pimenta do reino e sal a gosto"""
        
        yield """


Modo de preparo"""
        yield """
Corte sua carne em filés e depois em tiras largas. 
Reserve.
Em uma panela bem quente com um fio de azeite refogue a cebola e o alho.
Adicione a carne e deixe refogar, após agregue a couve chinesa e misture bem.
Siga adicionando o brócolis, o shoyu, o curry, a pimenta e o sal.
Desligue o fogo e por último misture a cebolinha verde e a castanha de caju. """

   
   
   
   
   
   
########                                                            #------SUINO------#                                                   ########
    
    @re_botcmd(pattern=r"^[Ss]u.*nos$")
    
    def Suino(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD
Bife de lombo
Lombo ao molho de maracujá """
 
    
    @re_botcmd(pattern=r"^[Bb]ife de [Ll]ombo.*$")
    def Bife_de_lombo(self, msg, match):
        self.send_stream_request(msg.frm, open('bifelombo.jpg', 'rb'), name='bifelombo.jpg', stream_type='photo')

        yield """Ingredientes
800g de lombo suíno em bifes
2 dentes de alho picados
1/2 xícara (chá) de vinho branco seco
Sal e pimenta-do-reino a gosto
4 colheres (sopa) de óleo
2 colheres (sopa) de manteiga
2 cebolas em rodelas
Cheiro-verde picado a gosto"""
        
        yield """

Modo de preparo"""
        yield """
Coloque o lombo em uma tigela, tempere com o alho, o vinho, sal, pimenta e deixe de molho por 1 hora. 
Aqueça uma frigideira grande com o óleo e frite os bifes, em fogo alto, por 3 minutos ou até dourarem. Retire, transfira para uma travessa e reserve. 
Volte a frigideira ao fogo médio com a manteiga e frite as cebolas até dourarem. 
Espalhe sobre os bifes e polvilhe com cheiro-verde. 
Sirva, se desejar, acompanhado com purê de batata."""

    
    @re_botcmd(pattern=r"^[Ll]ombo ao [Mm]olho de [Mm]aracuj.*$")
    def Lombo_ao_molho_de_maracuja(self, msg, match):
        self.send_stream_request(msg.frm, open('bifemaracuja.jpg', 'rb'), name='bifemaracuja.jpg', stream_type='photo')

        yield """Ingredientes
800g de lombo suíno em bifes
2 dentes de alho picados
1/2 xícara (chá) de vinho branco seco
Sal e pimenta-do-reino a gosto
4 colheres (sopa) de óleo
2 colheres (sopa) de manteiga
2 cebolas em rodelas
Cheiro-verde picado a gosto"""
        
        yield """

Modo de preparo"""
        yield """
Coloque o lombo em uma tigela, tempere com o alho, o vinho, sal, pimenta e deixe de molho por 1 hora. 
Aqueça uma frigideira grande com o óleo e frite os bifes, em fogo alto, por 3 minutos ou até dourarem. Retire, transfira para uma travessa e reserve. 
Volte a frigideira ao fogo médio com a manteiga e frite as cebolas até dourarem. 
Espalhe sobre os bifes e polvilhe com cheiro-verde. 
Sirva, se desejar, acompanhado com purê de batata."""


    
    
########                                                            #-----PEIXE------#                                                   ########
    
    @re_botcmd(pattern=r"^[Pp]eixe.*$")
    def Peixe(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD
Torta cremosa de sardinha
Peixe assado
Salmão com purê de mandioquinha
Bolinho de atum
Filé de peixe com manjericão
Camarões ao leite de coco        """


    
    @re_botcmd(pattern=r"^[Tt]orta [Cc]remosa de [Ss]ardinha.$")
    def Torta_cremosa_de_sardinha(self, msg, match):
        self.send_stream_request(msg.frm, open('tortasardinha.jpg', 'rb'), name='tortasardinha.jpg', stream_type='photo')

        yield """Ingredientes:
Massa

4 colheres (sopa) de leite
1 caixinha de creme de leite (200g)
3/4 xícara (chá) de óleo
4 ovos
1 colher (chá) de sal
1 xícara + 1/2 xícara (chá) de farinha de trigo
1 colher (sopa) de fermento em pó"""
            
        yield """      
Recheio"""
        yield """
3 latas de Sardinha
1 cebola grande em cubinhos
1 lata de milho verde (descarte a água)
1 tomate em cubinhos
Sal e pimenta do reino a gosto
3 colheres (sopa) de salsinha verde picada
1 colher (sopa) de cebolinha verde picada
2 colheres (sopa) de azeitona verde
1 xícara (chá) de maionese
1 colher (sopa) de azeite de oliva"""
            

        yield """

Modo de Preparo"""
            
        yield """

Recheio

Em uma tigela misture o milho, a cebola, o tomate, as azeitonas, salsinha e a cebolinha verde. A sardinha esmague com um garfo e adicione na tigela.
Tempere com sal e pimenta do reino. Acrescente a maionese e o azeite de oliva. 
Misture bem e reserve."""
            
        yield """

Massa
            
No liquidificador bata bem o óleo, o leite, o creme de leite, os ovos e o sal. 
Desligue o liquidificador e adicione a farinha de trigo e o fermento em pó. 
Misture apenas para incorporar.
Pegue uma forma untada e enfarinhada (ARO 23cm), despeje metade da massa, coloque todo recheio e por cima o restante da massa. 
Leve ao forno preaquecido a 180° por aproximadamente 45 minutos."""


    
    @re_botcmd(pattern=r"^[Pp]eixe [Aa]ssado.*$")
    def Peixe_assado(self, msg, match):
        self.send_stream_request(msg.frm, open('peixeassado.jpg', 'rb'), name='peixeassado.jpg', stream_type='photo')

        yield """Ingredientes
2 peixes frescos e limpos (truta)
2 batatas grandes descascadas e cortadas em fatias
1 cebola cortada em rodelas
1 pimenta dedo de moça picada
suco de 1 limão
4 fatias de limão
Coentro fresco
Sal e pimenta do reino à gosto """

        yield """

Modo de Preparo"""
        yield """
Cozinhe as batatas em água quente com sal. (não passe do ponto, elas devem estar firmes)
Comece fazendo cortes na superfície dos peixes dos dois lados.
Tempere com suco de limão, sal e pimenta do reino por fora e por dentro dos peixes. 
Ainda dentro coloque uma fatia de limão e folhas de coentro.
Em uma travessa regue um fio de azeite, disponha as batatas já cozidas e escorridas fazendo uma camada.
Por cima coloque as rodelas de cebola, pimenta dedo de moça picada (quem preferir menos picante deve retirar as sementes). 
Regue com azeite e disponha duas boas porções de coentro.
Disponha os peixes, e coloque uma fatia de limão em cima de cada um. 
Cubra a travessa com papel alumínio e leve ao forno preaquecido a 180° por aproximadamente 20 – 25 minutos. 
Nos últimos 5 minutos retire o papel alumínio e retorne ao forno para finalizar.
Sirva a seguir com uma bela farofa para acompanhar."""


    
    @re_botcmd(pattern=r"^[Ss]alm.* com [Pp]ur.* de [Mm]andioquinha$")
    def Salmao_com_pure_de_mandioquinha(self, msg, match):
        self.send_stream_request(msg.frm, open('salmao.jpg', 'rb'), name='salmao.jpg', stream_type='photo')

        yield """Ingredientes
Salmão grelhado
2 postas de salmão
suco de 1/2 limão
sal e pimenta do reino a gosto
Folhas de tomilho para decorar
Purê de mandioquinha
400g de mandioquinha
180ml de creme de leite fresco
Aproximadamente 120ml de leite
pitada de noz moscada
2 dentes de alho picados
sal a gosto
2 colheres (sopa) de manteiga
Azeite de oliva"""
        
        yield """

Modo de preparo"""
        yield """
Para o purê de mandioquinha: Descasque e corte em pedaços. 
Em uma panela com água quente e sal adicione as mandioquinhas.
Deixe cozinhar até amolecer (aproximadamente 20 minutos). 
Escorra, e passe elas ainda quente pelo espremedor, ou esmague com um garfo.
Em uma panela regue um fio de azeite, 1 colher de manteiga e o alho picado. 
Refogue. 
Acrescente a mandioquinha espremida, o creme de leite fresco, o leite, e tempere com noz moscada e uma pitadinha de sal. Misture. 
Adicione a outra colher de manteiga. 
Tampe e reserve."""
        
        yield """

Para o salmão"""
        yield """
Tempere as duas postas com suco de limão, sal e pimenta do reino dos dois lados.
Em uma frigideira antiaderente bem quente eu coloco a posta de salmão. 
Quando dourar já posso virar para dourar do outro lado.
No prato de servir coloque uma boa porção do purê e uma posta de salmão por cima. 
Decore com folhinhas de tomilho e sirva a seguir. """

    
    @re_botcmd(pattern=r"^[Bb]olinho de [Aa]tum.*$")
    def Bolinho_de_atum(self, msg, match):
        self.send_stream_request(msg.frm, open('bolinhoatum.jpg', 'rb'), name='bolinhoatum.jpg', stream_type='photo')

        yield """Ingredientes
2 latas de atum
1/2 cebola roxa picada
2 dentes de alho
1 fatia de pão de forma
1 colher (sopa) de leite
2 colheres (sopa) de fibra de trigo
1 colher (sopa) de farinha de trigo
1 ovo
1 colher (sopa) de molho de tomate
1 colher (sopa) de salsinha verde picada
sal e pimenta do reino a gosto
Óleo para fritar
Molho de tomate para acompanhar (opcional)"""

        yield"""

Para empanar"""
        yield """
Farinha de trigo
1 ovo batido
Quinoa em flocos ou farinha de rosca"""

        yield """

Modo de preparo"""
        yield """
Em uma tigela misture todos os ingredientes (a fatia de pão deve ser umedecida no leite antes de ser adicionada).
Pegue três pratos fundos, e coloque em cada um os ingredientes para empanar.
Siga fazendo bolinhas com a massa de atum, passe pela farinha de trigo, pelo ovo batido, pela quinoa em flocos ou farinha de rosca. Frite em óleo quente até dourar.
Se desejar, sirva um molho de tomate como acompanhamento do bolinho."""


    
    @re_botcmd(pattern=r"^[Ff]ile de [Pp]eixe com [Mm]anjeric.*$")
    def File_de_peixe_com_manjericao(self, msg, match):
        self.send_stream_request(msg.frm, open('manjericao.jpg', 'rb'), name='manjericao.jpg', stream_type='photo')

        yield """Ingredientes
4 filés de Saint Peter
3 dentes de alho triturados
Suco de 1 limão
Raspas de 1 limão
Pimenta do reino a gosto
Sal a gosto
Azeite a gosto
1 colher (chá) de orégano
2 colheres (sopa) de manjericão picado
1 xícara (chá) de mini tomates italianos cortados em 4 partes"""

        yield """

Modo de preparo"""
        yield """
Tempere os filés de saint peter com o suco de limão, as raspas do limão, o alho,  o manjericão,  a pimenta do reino e o sal, misture dos dois lados.
Em um refratário com um fio de azeite disponha os filés regue com azeite, nas laterais disponha os mini tomates cortados regados com azeite, sal e pimenta. 
Leve ao forno médio pré-aquecido 200° por aproximadamente 20 – 25 minutos.
Retire o refratário do forno e cubra cada filé com os mini tomates."""



    
    @re_botcmd(pattern=r"^[Cc]amar.*s ao [Ll]eite de [Cc]oco$")
    def Camaroes_ao_leite_de_coco(self, msg, match):   
        self.send_stream_request(msg.frm, open('camarao.jpg', 'rb'), name='camarao.jpg', stream_type='photo')
        yield """Ingredientes
300g de camarões grandes, descascados e limpos
Suco de 1 limão
1 colher (sopa) de manteiga
Sal e Pimenta do reino a gosto
1 pimenta dedo de moça
3 dentes de alho triturados
1 cebola picada
1 colher (sopa) de salsinha picada
1 colher (sopa) de cebolinha verde picada
1 colher (sopa) de coentro picado
1/4 colher (chá) de cominho em pó
1 colher (chá) de páprica
1 vidro de leite de coco (200ml)"""
        

        yield """

Modo de preparo"""
        yield """
Tempere os camarões com limão, sal, pimenta e alho. 
Deixe marinando por aproximadamente 1 hora.
Em uma panela derreta a manteiga e refogue a cebola até que fique transparente, adicione a pimenta dedo de moça (picada e sem sementes). 
Acrescente os camarões e doure rapidamente dos dois lados.
Adicione o leite de coco, a páprica, o cominho e tempere com sal e pimenta.
Deixe o molho apurar alguns minutos.
Finalize acrescentando a cebolinha verde, a salsinha e o coentro"""


   








#--------------------------------------------------------------------------VEGETARIANAS--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#   
    
    @re_botcmd(pattern=r"^[Vv]egetarianas.*$")
    def Vegetarianas(self, msg, match):
        yield """Ok, estamos quase lá… escolha um dos pratos principais:
Salada Grega
Berinjela com vinagrete de azeite
Nhoque de ricota e espinafre
Strogonoff de cogumelos
Polenta cremosa com gorgonzola
Torta de brócolis
Torta de palmito com requeijão"""
     
    
    @re_botcmd(pattern=r"^[Ss]alada [Gg]rega.*$")
    def Salada_Grega(self, msg, match):
        self.send_stream_request(msg.frm, open('grega.jpg', 'rb'), name='grega.jpg', stream_type='photo')
        yield """Ingredientes
1 pé pequeno de alface lisa ou romana
2 tomates holandeses partidos em gomos
1 pepino caipira pequeno descascado e sem sementes
1 cebola roxa pequena em gomos
50 g de azeitona preta sem caroço
50 g de azeitona verde pequena sem caroço
50 g de queijo feta
½ xícara (chá) de vinagrete de limão e salsinha"""
                
        yield """


Modo de Preparo"""
        yield """     
Lave as folhas de alface, seque e parta ao meio.
Disponha em uma tigela e junte os tomates, o pepino, a cebola, as azeitonas (pretas e verdes), o queijo feta e o vinagrete de limão e salsinha. """

    
    @re_botcmd(pattern=r"^[Bb]erinjela com [Vv]inagrete de [Aa]zeite.*$")
    def Berinjela_com_vinagrete_de_azeite(self, msg, match):
        self.send_stream_request(msg.frm, open('beringela.jpg', 'rb'), name='beringela.jpg', stream_type='photo')
        yield """Ingredientes
1 ramo de cebolinha (francesa ou cebolete) picada
4 colheres (sopa) de azeite intenso
1 quilo de mini berinjela ou de berinjela pequena, cortada ao meio ou em rodelas
Sal a gosto
2 echalotes fatiadas bem fino
Suco de 1 limão"""
        
        yield """

Modo de preparo"""
        yield """
Em uma assadeira, disponha as metades de berinjela.
Tempere com sal e leve ao forno médio preaquecido a 180ºC por 15 minutos.
Enquanto isso, prepare o vinagrete misturando em uma tigela as fatias de echalote, a cebolinha, o suco de limão e o azeite.
Despeje sobre as berinjelas assadas e sirva como acompanhamento de carnes grelhadas ou frango assado."""


    
    @re_botcmd(pattern=r"^[Nn]hoque de [Rr]icota e [Es]spinafre.*$")
    def Nhoque_de_ricota_e_espinafre(self, msg, match):
        self.send_stream_request(msg.frm, open('ricota.jpg', 'rb'), name='ricota.jpg', stream_type='photo')
        yield """Ingredientes
1,5 maço de espinafre fresco
30 g de manteiga integral sem sal
50 g de cebola pera
300 g de ricota fresca
100 g de farinha de trigo
2 gemas de ovo
50 g de queijo grana padano
Sal a gosto
Noz-moscada a gosto"""

        yield """

Modo de Preparo"""
        yield """
Limpar o espinafre, eliminando os talos. 
Cozinhar as folhas em água fervente por 30 segundos. 
Escorrer, resfriar e espremer bem para eliminar toda a água. Picar bem.
Em uma frigideira, colocar a manteiga, adicionar a cebola em cubinhos e cozinhar por alguns minutos.
Acrescentar o espinafre e saltear um pouco.
Em uma tigela, colocar a ricota e amassar bem. 
Adicionar o espinafre salteado, a farinha, as gemas e queijo ralado e temperar com sal e noz-moscada.
Misturar bem até formar uma massa homogênea.
Fazer bolinhas de cerca de 1 cm com a massa de ricota e espinafre e cozinhar em abundante água fervente salgada.
Servir os nhoque com molho de tomate e queijo ralado.
"""

    
    @re_botcmd(pattern=r"^[Ss]trogonoff de [Cc]ogumelos.*$")
    def Strogonoff_de_cogumelos(self, msg, match):
        self.send_stream_request(msg.frm, open('cogumelos.jpg', 'rb'), name='cogumelos.jpg', stream_type='photo')
        yield """Ingredientes
3 colheres (sopa) de azeite
1 cebola roxa cortada em cubos
2 dentes de alho espremidos
500 g de cogumelos variados (shiitake, shimeji, portobelo e champignons)
2 colheres (sopa) de suco de limão
1 colher (sopa) de catchup
400 ml de caldo de legumes
1 colher (sopa) de amido de milho dissolvido em água fria
100 g de creme de leite
½ xícara (chá) de iogurte desnatado
3 colheres (sopa) de salsinha picada
Arroz branco para acompanhar
Batata palha"""


        yield """

Modo de Preparo

Em uma panela com o azeite, refogue a cebola e o alho até que a cebola comece a murchar. Junte os cogumelos, o limão, e o catchup. 
Cozinhe por 5 a 10 minutos.
Adicione o caldo e cozinhe por mais 5 minutos. 
Junte a maisena e deixe ferver até engrossar ligeiramente. 
Por último, adicione o creme de leite, tempere e junte a salsinha. 
Sirva com arroz e batata palha."""


    
    @re_botcmd(pattern=r"^[Pp]olenta [Cc]remosa com [Gg]orgonzola.*$")
    def Polenta_cremosa_com_gorgonzola(self, msg, match):
        self.send_stream_request(msg.frm, open('gorgonzola.jpg', 'rb'), name='gorgonzola.jpg', stream_type='photo')
        yield """Ingredientes
1 ½ xícara (chá) de fubá
2 xícaras (chá) de leite
3 xícaras (chá) de água
50g de manteiga sem sal
100g de queijo gorgonzola
Sal a gosto"""
        
        yield """

Modo de Preparo

Dissolva o fubá no leite. 
Coloque a água na panela de pressão, junte o fubá dissolvido, a manteiga e o sal.
Leve ao fogo e mexa até a manteiga derreter, a polenta engrossar e começar a ferver. 
Tampe a panela e, assim que pegar pressão, abaixe o fogo e deixe cozinhar por 15 minutos. Esfrie a panela, abra e misture bem. 
Sirva imediatamente em pratos individuais e cubra com o queijo gorgonzola em pedacinhos. """
     
    
    @re_botcmd(pattern=r"^[Tt]orta de [Bb]r.*colis.*$")
    def Torta_de_brocolis(self, msg, match):
        self.send_stream_request(msg.frm, open('brocolis.jpg', 'rb'), name='brocolis.jpg', stream_type='photo')
        yield """Ingredientes
Massa
        
½ xícara de água
1ovo
3 colheres de sopa de azeite
1 colher de chá de sal
1 colher de sobremesa de fermento em pó
Farinha integral o suficiente"""
        
        yield """

Cobertura

1 molho de brócolis
1 cebola
2 colheres de sopa de azeite
1 tomate descascado e picado"""

        yield """

Modo de Preparo

Misturar tudo e forrar uma forma com essa massa
Colocar uma panela no fogo com água
Assim que ferver acrescentar um pouco de sal e o brócolis
Deixar cozinhar durante dois minutos e escorrer
Refogar a cebola picada no azeite e acrescentar o brócolis, deixar no fogo durante alguns minutos
Bater no liquidificador 2 ovos, ½ xícara de água, 3 colheres de queijo ralado, 1 colher de sopa de amido de milho. """


    
    @re_botcmd(pattern=r"^[Tt]orta de [Pp]almito com [Rr]equeij.*$")
    def Torta_de_palmito_com_requeijao(self, msg, match):
        self.send_stream_request(msg.frm, open('palmito.jpg', 'rb'), name='palmito.jpg', stream_type='photo')
        yield """Ingredientes
Massa

2 xícaras (chá) de farinha de trigo        
1 lata de creme de leite sem soro
150 g de margarina
1 colher (chá) de sal
1 gema + 1 gema para pincelar"""

        yield """

Recheio

3 colheres (sopa) de azeite
1 colher (sopa) de farinha de trigo
1 vidro grande de palmito
1 cebola picada
1 tomate picado
1/2 xícara (chá) de cheiro-verde
1/2 xícara (chá) de azeitonas
1 pote de requeijão
sal a gosto"""

        yield """

Modo de preparo- recheio

Para isso, aqueça uma panela com o azeite.
Em seguida, acrescente a cebola e o tomate picado e refogue bem.
Assim que eles murcharem, adicione o palmito, as azeitonas e o sal a gosto.
Cozinhe em fogo médio por alguns minutos.
Adicione o requeijão, a farinha de trigo e o cheiro-verde.
Mexa bem e espere levantar fervura.
Transfira o recheio para um recipiente e leve para a geladeira."""

        yield """

Modo de preparo- massa

Em uma tigela, coloque a farinha de trigo, a margarina, o sal, uma gema e o creme de leite.
Com as mãos, misture bem até obter uma massa lisa e homogênea.
Se necessário, acrescente um pouco mais de farinha.
Cubra a tigela com um pano e deixe descansar por 15 minutos.
Na sequência, abra a massa com ajuda de um rolo.
Use-a para forrar o fundo e as laterais de uma forma de fundo removível.
Reserve um círculo de massa para fechar a torta.
Coloque o recheio frio dentro da torta e cubra-a com o círculo de massa.
Finalize pincelando uma gema por cima da massa.
Leve para assar em forno preaquecido a 210º C por 40 minutos ou até que a torta esteja dourada.   """


#-----------------------------------------------------------------------VEGANAS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



    
    @re_botcmd(pattern=r"^[Vv]eganas [Dd]oces.*$")
    def Veganas_Doces(self, msg, match):
        yield """Ok, estamos quase lá… escolha um dos pratos principais:
\Moqueca de banana-da-terra vegana
\Bolo de cenoura vegano
\Brigadeiro vegano
\Biscoitinhos veganos
\Bolo de banana vegano """

            
    
    @re_botcmd(pattern=r"^[Mm]oqueca de [Bb]anana da [Tt]erra [Vv]egana.*$")
    def Moqueca_de_banana_da_terra_vegana(self, msg, match):
        self.send_stream_request(msg.frm, open('moqueca.jpg', 'rb'), name='moqueca.jpg', stream_type='photo')
        yield """Ingredientes
6 bananas-da-terra sem casca
suco coado de 1 limão
1 dente de alho picado
3 pimentas dedo-de-moça, sem sementes, picadas
Sal e pimenta-do-reino branca moída na hora
2 colheres (sopa) de azeite
2 cebolas grandes cortadas em rodelas finas
1 pimentão amarelo sem sementes em rodelas
1 pimentão verde sem sementes em rodelas
1 pimentão vermelho sem sementes em rodelas
1 lata de tomate pelado
1 1/3 xícara de leite de coco
2 colheres (sopa) de cheiro-verde picado"""
        
        yield """

Modo de preparo"""
        yield"""
Corte a banana no sentido do comprimento e depois em pedaços grandes. 
Ponha em uma tigela com o suco de limão, o alho, a pimenta dedo-de-moça, o sal e a pimenta-do-reino. 
Reserve por uma hora e meia. 
Em seguida, aqueça o azeite em uma panela grande e refogue a cebola e os pimentões. 
Acrescente o tomate pelado ligeiramente picado com o conteúdo da lata e cozinhe por 5 minutos. Por cima, arrume a banana com sua marinada. 
Cubra com o leite de coco e polvilhe com metade do cheiro-verde. 
Cozinhe, mexendo às vezes com cuidado, por mais 25 minutos ou até a banana ficar macia e o líquido se reduzir bem. 
Sirva em seguida, polvilhada com o cheiro-verde restante."""
        

    
    @re_botcmd(pattern=r"^[Bb]iscoitinhos [Vv]eganos.*$")
    def Biscoitinhos_veganos(self, msg, match):
        self.send_stream_request(msg.frm, open('biscoitinhos.jpg', 'rb'), name='biscoitinhos.jpg', stream_type='photo')
        yield """Ingredientes
1 colher (sobremesa) raspas de laranja (opcional)
1 xícara (chá) farinha de trigo branca
1 xícara (chá) Farinha de Trigo Integral Fina
1 xícara (chá) de amido de milho    
200 gr gordura de palma ou de coco
1 pitada de sal
1 colher (café) extrato ou essência de baunilha
1 xícara (chá) açúcar branco, mascavo, cristal orgân ou demerara
2 colheres (sopa) água"""
        
        yield """

Modo de preparo"""
        yield """
Misture a água com o açúcar escolhido (quanto mais fino o açúcar, mais liso e doce o biscoito. 
Ao mesmo tempo, o uso de um açúcar demerara - que irá dissolver pouco - agrega uma crocância interessante ao biscoito e pontos de doçura.
Você pode usar meio a meio).  
Misture a essência e raspas, farinhas e gordura, trabalhando a massa até ficar homogênea. 
Cubra com filme e deixe descansar em geladeira por 2 horas.             
Polvilhe uma superfície com amido e abra com rolo até uma espessura de 1,5cm. 
Dê formato com cortadores, marcadores ou até mesmo copos de boca mais fina.             
Asse em tabuleiro polvilhado com farinha (ou coberto por silpat ou papel manteiga) por 30 minutos na temperatura de 180ºC, até dourar. 
Espere os biscoitos esfriarem para manuseá-los, decorá-los, etc. """

    
    @re_botcmd(pattern=r"^[Bb]olo de [Bb]anana [Vv]egano.*$")
    def Bolo_de_banana_vegano(self, msg, match): 
        self.send_stream_request(msg.frm, open('bolobanana.jpg', 'rb'), name='bolobanana.jpg', stream_type='photo')
        yield """ngredientes
1 xícara (chá) de coco ralado
1 e 1/3 xícaras de óleo vegetal
1 e 1/2 xícaras de açúcar
6 unidades de banana
3/4 colher (chá) de sal
2 colheres (chá) de fermento químico em pó
3 xícaras (chá) de farinha de trigo
1 colher (sopa) de canela-da-china em pó
1/2 xícara (chá) de água"""
        
        yield """

Modo de preparo"""
        yield """
Misture farinha, fermento e sal com a ajuda de um fouet em um recipiente. 
Misture óleo, açúcar e banana em outro recipiente.             
Junte as duas massas.             
Acrescente o coco, a canela e a água.             
Bata tudo com a ajuda de uma colher de pau ou uma batedeira.
Coloque toda a massa numa forma de furo untada e leve ao forno pré aquecido por 20 minutos em forno médio. 
Aguarde 40 a 60 minutos, a depender a potência do seu forno ou até o palito ou a faca inserida na massa sair limpo/a.             
Ao desenformar polvilhe com canela e açúcar."""
            
            
    
    
    
    
### Separação AntiBug    
  
  
    
    @re_botcmd(pattern=r"^[Vv]eganas [Ss]algadas.*$")
    def Veganas_Salgadas(self, msg, match):
        yield """Ok, estamos quase lá… escolha um dos pratos principais:
\Salada de gravatinha com maionese de cenoura vegana
\Caldo de legumes
\Patê de ervilha vegano
\Carne de soja vegana refogada 
\Creme de milho vegano
"""

    
    @re_botcmd(pattern=r"^[Ss]alada de [Gg]ravatinha com [Mm]aionese de [Cc]enoura [Vv]egana.*$")
    def Salada_de_gravatinha_com_maionese_de_cenoura_vegana(self, msg, match):
        self.send_stream_request(msg.frm, open('saladadegravatinha.jpg', 'rb'), name='saladadegravatinha.jpg', stream_type='photo')
        yield """Ingredientes
Salada

1 xícara de macarrão gravatinha integral e vegano cozido al dente
¼ de xícara de azeitona verde, sem caroço, cortada em rodelas
1/3 de xícara de ervilha descongelada
4 tomates-cereja cortados ao meio
3 castanhas-do-pará picadas
1/3 de xícara de vagem cozida e cortada em pedaços
1/3 xícara de cenoura, sem casca, cozida e cortada em rodelas
½ colher (sopa) de linhaça dourada
1 colher (sopa) de azeite
uma pitada de sal rosa"""
        
        yield """


Maionese"""
        yield """
2 cenouras pequenas, sem casca, cozidas
1 chuchu cozido, sem a casca e sem o miolo
2 colheres (sopa) de azeite
1 colher (chá) de alho e cebola desidratados
1 pitada de cúrcuma"""
        
        yield """

Modo de preparo"""
        yield """
Em uma tigela, misture todos os ingredientes da salada e transfira para um pote. 
Tampe e leve à geladeira por, no mínimo, 8 horas. 
Para fazer a maionese, bata todos
os ingredientes no liquidificador. 
Sirva com a salada. 
Se quiser incrementá-la, adicione uma batata sem casca cozida e 2 colheres (sopa) de leite de aveia."""


    
    @re_botcmd(pattern=r"^[Cc]aldo de [Ll]egumes.*$")
    def Caldo_de_legumes(self, msg, match):
        self.send_stream_request(msg.frm, open('caldodelegumes.jpg', 'rb'), name='caldodelegumes.jpg', stream_type='photo')
        yield """Ingredientes:
2 cenouras
2 talos de salsão
1 cebola grande
2 folhas de louro
5 grãos de pimenta preta
1 colher (chá) de sal
Aproximadamente 2 litros de água
Opcional: Cravo, Anis ou Ervas da sua preferência"""
            
        yield """

Modo de Preparo"""
        yield """
Em uma panela grande coloque a cebola cortada em quatro partes, a cenoura descascada e cortada em pedaços, o salsão picado, as folhas de louro e a pimenta em grãos. 
Despeje a água. Ligue o fogo. 
Quando levantar fervura despeje o sal, misture.
Abaixe o fogo e deixe cozinhando por 40 minutos.
Após, passe pela peneira e seu caldo de legumes estará pronto."""

   
   
   
    
    @re_botcmd(pattern=r"^[Bb]olinho [Aa]ssado de [Gg]r.* de [Bb]ico [Vv]egano$")
    def Bolinho_assado_de_grao_de_bico_vegano(self, msg, match):
        self.send_stream_request(msg.frm, open('bolinhoassado.jpg', 'rb'), name='bolinhoassado.jpg', stream_type='photo')
        yield """Ingredientes"""
        yield """
Bolinho"""
        yield """
1½ xícara de grão-de-bico demolhado e cozido
1 cebola roxa pequena picada
1 dente de alho
1 colher (sopa) de azeite, e mais um pouco para untar
½ colher (sopa) de tahine
1 colher (sopa) de cebolinha picada
uma pitada de pimenta síria
Sal a gosto
Pimenta-do-reino branca moída na hora a gosto
4 colheres (sopa) de farinha de trigo integral"""
        

        yield """

Molho"""
        yield """
1 colher (sopa) de suco de limão-siciliano
1 dente de alho picado
1 cebola pequena picada
1 colher (sopa) de azeite
Cebolinha picada a gosto para salpicar"""
        
        yield """

Modo de preparo"""
        yield """
Preaqueça o forno a 180 °C. 
Bata o grão-de-bico no processador junto com os demais
ingredientes, exceto a farinha. 
Transfira para uma tigela e junte a farinha, misturando bem até soltar das mãos. 
Forme bolinhos achatados. 
Forre uma assadeira com papel-alumínio e unte-o com azeite. 
Distribua os bolinhos e asse por 40 minutos ou até dourarem, virando na metade do tempo.
Para fazer o molho, bata todos os ingredientes no liquidificador, exceto a cebolinha. 
Salpique-a e sirva o molho com os bolinhos. Sirva com quinoa com cenoura  e escarola refogada."""

    
    
    
    
    @re_botcmd(pattern=r"^[Pp]at.* de [Ee]rvilha [Vv]egano$.*$")
    def Pate_de_ervilha_vegano(self, msg, match):
        self.send_stream_request(msg.frm, open('paredeervilha.jpg', 'rb'), name='paredeervilha.jpg', stream_type='photo')
        yield """Ingredientes
1 xícara de ervilha seca demolhada e cozida al dente
1 dente de alho pequeno
1 cebola pequena
½ xícara de castanha de caju, sem sal, demolhada e bem escorrida
3 colheres (sopa) de azeite
1 colher (sopa) de suco de limão-siciliano coado
Sal e pimenta-do-reino branca moída na hora a gosto"""
        
        yield """

Modo de preparo"""
        yield """
Para demolhar a castanha de caju, coloque-a em uma tigela, cubra com água filtrada e deixe por, no mínimo, 8 horas. 
Passado esse tempo, escorra a castanha e descarte a água. 
Bata todos os ingredientes no liquidificador até obter uma massa homogênea.
Sirva."""
    
    

    @re_botcmd(pattern=r"^[Cc]arne de [Ss]oja [Vv]egana [Rr]efogada.*$")
    def Carne_de_soja_vegana_refogada(self, msg, match):
        self.send_stream_request(msg.frm, open('carnedesoja.jpg', 'rb'), name='carnedesoja.jpg', stream_type='photo')
        yield """Ingredientes
1 xícara (chá) de proteína de soja
2 xícaras (chá) de água fervente
sal a gosto
salsinha picada(s) a gosto
1/2 unidade de cebola picada(s)
1 dente de alho picado(s)
2 unidades de tomate sem semente(s)
1 colher (sopa) de óleo de soja"""
        
        yield """

Modo de preparo"""
        yield """
Coloque a proteína de soja em um recipiente e cubra com água fervente.
Em seguida escorra-a em uma peneira,retirando o excesso de água com o auxílio de uma colher,apertando-a contra a peneira.             
Tempere a proteína de soja com os tomates picados,a cebola picada,o alho picado,a salsinha picada e o sal.             
Coloque o óleo em uma panela e refogue a proteína até ficar levemente dourada.     """
 
    
    @re_botcmd(pattern=r"^[Cc]reme de [Mm]ilho [Vv]egano.*$")
    def Creme_de_milho_vegano(self, msg, match):
        self.send_stream_request(msg.frm, open('cremedemilho.jpg', 'rb'), name='cremedemilho.jpg', stream_type='photo')
        yield """Ingredientes
400 gr de milho verde (2 latas)
4 colheres (sopa) de farinha de aveia
4 colheres (sopa) de azeite (ou outro óleo vegetal de sua preferência)
4 folhas de manjericão (ou a gosto)
1 colher (sobremesa) de orégano seco
sal a gosto
castanha-do-pará (opcional) a gosto"""
        
             
        yield """        
Modo de preparo """

        yield """
Junte a aveia a meia xícara de água e mexa até obter um leite vegetal.             
Bata todos os ingredientes em um mixer.             
Pronto.             
Não é necessário levar ao fogo, mas você pode fazer isso se quiser engrossar um pouco mais.             
        """  
    



#----------------------------------------------------------------------------SALADAS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------# 
    
    @re_botcmd(pattern=r"^[Ss]aladas.*$")
    def saladas(self, msg, match):
        yield """Ok, estamos quase lá… escolha um dos pratos principais:
\Salada de feijão fradinho com bacalhau
\Salada de batata com presunto
\Salada de repolho com abacaxi
\Salada Primavera de Morangos
\Salada de Acelga"""

    
    @re_botcmd(pattern=r"^[Ss]alada de [Ff]eij.* [Ff]radinho com [Bb]acalhau$")
    def Salada_de_feijao_fradinho_com_bacalhau(self , msg, match):
        self.send_stream_request(msg.frm, open('saladafradinho.jpg', 'rb'), name='saladafradinho.jpg', stream_type='photo')
        yield """Ingredientes
500 g de feijão-fradinho cozido
500 g de bacalhau escaldado e desfiado em pedaços médios
3 cebolas picadas em rodelas finas
3 tomates sem sementes picados em cubos pequeno
2 pimentões verdes picados em tiras finas
2 pimentões vermelhos picados em tiras finas
8 dentes de alho amassados
5 colheres (sopa) de azeite
100 g de azeitonas picada
1 xícara (chá) de suco de limão
1 xícara (chá) de cheiro-verde picado
1/2 xícara (chá) de azeite
orégano a gosto
1 pitada de manjericão desidratado
sal a gosto"""
        
        yield """

Modo de preparo"""

        yield """
Em uma panela grande, esquente o azeite e refogue o alho e a cebola
Em seguida, adicione os pimentões
Depois de aproximadamente 1 minuto refogando os pimentões, acrescente o bacalhau, o suco de limão, as azeitonas, o sal, o orégano, o cheiro-verde e o manjericão, misturando bem
Desligue o fogo, acrescente o feijão-fradinho já cozido e os tomates e misturar delicadamente para que os vegetais não se desfaçam
Coloque essa mistura em uma travessa, regue com mais azeite e sirva."""

    
    @re_botcmd(pattern=r"^[Ss]alada de [Bb]atata com [Pp]resunto.*$")
    def Salada_de_batata_com_presunto(self, msg, match):
        self.send_stream_request(msg.frm, open('saladadebatatacompresunto.jpg', 'rb'), name='saladadebatatacompresunto.jpg', stream_type='photo')
        yield """Ingredientes
600 g de batatas
100g de presunto cortado em fatias
1 copo de iogurte natural
4 colheres de sopa de creme de leite
colorau
sal
cebolinha verde"""
        

        yield """
 
Modo de preparo"""

        yield """

Misture o creme de leite com uma pitada de colorau, iogurte e sal
Reserve
Cozinhe as batatas com cascas
Depois de macias, descasque e corte em pedaços
Corte o presunto em quadradinhos
Em uma saladeira ponha as batatas, o presunto e adicione o molho
Salpique a cebolinha
Deixe em temperatura ambiente até a hora de servir."""

    
    @re_botcmd(pattern=r"^[Ss]alada de [Rr]epolho com [Aa]bacaxi.*$")
    def Salada_de_repolho_com_abacaxi(self, msg, match):
        self.send_stream_request(msg.frm, open('saladaderepolhocomabacaxi.jpg', 'rb'), name='saladaderepolhocomabacaxi.jpg', stream_type='photo')
        yield """Ingredientes
1 repolho branco
1 repolho roxo
Abacaxi (a gosto)
Passas (a gosto)
1 sazón para salada
1/2 vidro gande de maionese (ou a gosto)
1/2 caixa de creme de leite (ou a gosto)
1 cebola"""
        
        yield"""

Modo de preparo"""

        yield """

Pique o abacaxi em cubos pequenos, passe na peneira deixando escorrer bem e reserve
Pique os repolhos bem finos e reserve
Pique a cebola em cubos bem pequenos e reserve
Misture todos os ingredientes
Acrescente o creme de leite e a maionese, misture
Acrescente as passas e o tempero
Decore com ameixas
Sirva gelada."""
            
    
    @re_botcmd(pattern=r"^[Ss]alada [Pp]rimavera de [Mm]orangos.*$")
    def Salada_Primavera_de_morangos(self, msg, match):
        self.send_stream_request(msg.frm, open('saladaprimaverademorangos.jpg', 'rb'), name='saladaprimaverademorangos.jpg', stream_type='photo')
        yield """Ingredientes
Salada

1/2 kg de morango
1 pé pequeno de alface americana
1 xícara (chá) de cogumelos frescos fatiados
3 colheres (sopa) de cebolinha picada
4 colheres (sopa) de amêndoas torradas em lascas"""
        
        yield """
Molho"""

        yield """
1 colher (sopa) de vinagre de maçã
1 colher (chá) de mel
1 colher (chá) de Fondor MAGGI
1 colher (sopa) de azeite
1 colher (chá) de sementes de papoula"""
        
        yield """

Modo de preparo"""

        yield """

Limpe os morangos e corte-os em quatro
Reserve 1/2 xícara (chá) para o preparo do molho
Lave a alface, deixe secar um pouco e corte-a em tiras finas
Afervente rapidamente os cogumelos, escorra e reserve
Em uma saladeira ou em pratos individuais, disponha a alface, os morangos, os cogumelos, a cebolinha e as amêndoas
À parte, amasse com um garfo o morango reservado e acrescente os ingredientes do molho
Regue a salada com o molho e sirva."""


    
    @re_botcmd(pattern=r"^[Ss]alada de [Aa]celga.*$")
    def Salada_de_Acelga(self, msg, match):
        self.send_stream_request(msg.frm, open('saladadeacelga.jpg', 'rb'), name='saladadeacelga.jpg', stream_type='photo')
        yield """Ingredientes
Salada

1 maço de acelga
1 cenoura cortada a julienne
4 colheres (sopa) de azeitonas pretas em rodelas"""
        
        yield """

Molho"""

        yield """
1 pote de Iogurte Natural Integral
2 colheres (sopa) de folhas de hortelã picadas
1/2 colher (chá) de MAGGI® FONDOR"""
        
        yield """
  
Modo de preparo"""

        yield """
Em uma travessa, coloque a acelga com a cenoura e a azeitona preta
Reserve. """
            

#----------------------------------------------------------------------------RISOTOS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    @re_botcmd(pattern=r"^[Rr]isotos.*$")
    def Risotos(self, msg, match):
        yield """Ok, estamos quase lá… escolha um dos pratos principais:
\Risoto simples de frango
\Arroz com champanhe
\Risoto de brócolis com queijo minas
\Risoto de salmão
\Risoto quatro queijos
\Risoto de palmito"""

            
    
    @re_botcmd(pattern=r"^[Rr]isoto [Ss]imples de [Ff]rango.*$")
    def Risoto_simples_de_frango(self, msg, match):
        self.send_stream_request(msg.frm, open('risotosimplesdefrango.jpg', 'rb'), name='risotosimplesdefrango.jpg', stream_type='photo')
        yield """Ingredientes
3 dentes de alho amassados
1 xícara (chá) de cebola picada
1 colher (sopa) de óleo
1 1/2 xícara (chá) de arroz lavado e escorrido
Sal e pimenta do reino a gosto
1 xícara (chá) de frango cozido e desfiado
3 xícaras (chá) de água fervente
200g de salsichas ferventadas e picadas
2 colheres (sopa) de extrato de tomate"""
        
        yield """

Modo de preparo"""

        yield """
Em uma panela, em fogo médio, frite o alho e a cebola no óleo.
Acrescente o arroz, tempere com sal e pimenta e continue fritando.
Coloque o frango, a água e o extrato de tomate.
Abaixe o fogo e deixe cozinhar até secar a água, com a panela semi tampada.
Desligue o fogo, misture as salsichas, deixe descansar por 15 minutos e sirva."""

     
    @re_botcmd(pattern=r"^[Aa]rroz com [Cc]hampanhe.*$")
    def Arroz_com_champanhe(self, msg, match):
        self.send_stream_request(msg.frm, open('arrozcomchampanhe.jpg', 'rb'), name='arrozcomchampanhe.jpg', stream_type='photo')
        yield """Ingredientes
1 dente de alho espremido
150 g de manteiga
4 xícaras (chá) de arroz agulha lavado e seco
250 g de champignon fatiado
1 tabletes de caldo de galinha dissolvidos em água quente (3 xícaras)
sal a gosto
200 g de amêndoas sem pele trituradas e picadas (opcional)
salsa picada para salpicar
1 xícara (chá) de parmesão ralado
2 xícaras (chá) de champanhe ou outro espumante"""
        
        yield """

Modo de preparo"""
 
        yield """
Comece derretendo a manteiga em uma panela e refogue todo o alho.
Acrescente o champignon e refogue bem rápido.
Coloque o arroz e misture muito bem, deixe refogar mais uma vez.
Adicione o tablete de caldo dissolvido na água quente e mexa.
Ajuste o sal, tampe e deixe cozinhando até que a água seque por completo (cerca de 15 minutos).
Regue com champanhe, tampe novamente e deixe secar.
Depois salpique o parmesão e mexa tudo com a ajuda de um garfo.
Finalize com as amêndoas e a salsinha (opcional) e sirva em seguida. 
"""
        
            
    
    @re_botcmd(pattern=r"^[Rr]isoto de [Bb]roc.*lis com [Qq]ueijo.*$")
    def Risoto_de_brocolis_com_queijo(self, msg, match):
        self.send_stream_request(msg.frm, open('risotobrocolis.jpg', 'rb'), name='risotobrocolis.jpg', stream_type='photo')
        yield """Ingredientes
400 g de arroz arbóreo
200 g de brócolis sem os talos
100 g de queijo minas meia cura cortado em cubinhos
1 e 1/2 litro de caldo de frango
1/2 xícara (chá) de vinho branco seco
2 colheres (sopa) de manteiga
4 colheres (sopa) de queijo parmesão ralado
1 cebola média bem picada
3 dentes de alho amassados
sal e pimenta-do-reino a gosto"""
        
        yield """

Modo de preparo"""

        yield """

Aqueça uma panela com metade da manteiga e acrescente a cebola.
Refogue em fogo médio até que ela fique translúcida e macia, mas sem dourar.
Adicione o arroz e refogue por alguns minutos.
Despeje o vinho branco, aumente o fogo e deixe-o secar.
Assim que secar, coloque um pouco do caldo de frango quente e mexa de vez em quando até secar.
Conforme o caldo for secando, acrescente mais.
Quando estiver na metade do caldo, adicione o brócolis e continue o cozimento até acabar o caldo e o arroz estar al dente.
Na sequência, adicione o queijo minas meia cura picadinho e misture bem.
Cozinhe por mais 2 minutos ou até o queijo começar a derreter e desligue o fogo.
Acrescente a manteiga, o parmesão, o sal e a pimenta e misture bem.
Sirva em seguida.        
        """
            
    
    @re_botcmd(pattern=r"^[Rr]isoto de [Ss]alm.*$")
    def Risoto_de_salmao(self, msg, match):
        self.send_stream_request(msg.frm, open('risotosal.jpg', 'rb'), name='risotosal.jpg', stream_type='photo')
        yield """Ingredientes
200 g de arroz para risoto
100 g de salmão ao natural
1/4 de cebola picada
150 ml de vinho branco
        self.send_stream_request(msg.frm, open('.jpg', 'rb'), name='.jpg', stream_type='photo')
1 colher de sopa de margarina
Óleo de oliva extra virgem
Sal e pimenta a gosto
Salsinha picada
1 litro de água morna
2 colheres de sopa de queijo ralado"""
        
        yield """

Modo de preparo """

        yield """
O segredo do risoto é usar fogo médio e mexer sempre sem parar entre 16 e 18 minutos
Coloque em uma frigideira média o óleo de oliva e a cebola picada para refogar por 30 segundos em fogo médio
Em seguida coloque o arroz para risoto e mexa sem parar com uma colher de pau pegando todos os lados
Coloque a água em pequenas doses de modo que cubra o risoto levemente e continue mexendo
Quando a água "evaporar" quase que na totalidade coloque mais água novamente e mexa sempre lentamente, esse processo deve durar 13 minutos, em seguidacoloque o vinho e continue mexendo
Logo depois de mexer bem coloque o salmão bem picado e continue mexendo, quando faltar 2 minutos para acabar coloque a margarina e em seguida o queijoralado e não coloque mais água, já que neste momento o arroz já está no ponto e bem mole, acrescente sal e pimenta a gosto e a salsinha picada."""


    
    @re_botcmd(pattern=r"^[Rr]isoto [Qq]uatro [Qq]ueijos.*$")
    def Risoto_quatro_queijos(self, msg, match):
        self.send_stream_request(msg.frm, open('risotoquatroqueijos.jpg', 'rb'), name='risotoquatroqueijos.jpg', stream_type='photo')
        yield """Ingredientes
2 colheres (sopa) de margarina
1 dente de alho picadinho
3 copos (americano) de arroz para risoto
1 litro de água
3 sachês de tempero pronto de sua escolha
1 colher (sopa) de requeijão
1 peça pequena de queijo gorgonzola
1 peça pequena de queijo parmesão
1 peça pequena de queijo gouda
Os queijos podem ser substituídos por outros de sua preferência"""
        
        yield """

Modo de preparo"""

        yield """
Despeje os temperos na água e coloque para ferver
Corte os queijos em cubinhos
Em uma panela, coloque o arroz, o alho picadinho e uma colher de margarina, deixe fritar por aproximadamente 5 minutos
Adicione uma pequena quantidade de água e mexa até secar a água
Então, repita este procedimento por 40 minutos, sempre mexendo o arroz para não grudar
O arroz deverá ficar aldente, mas não duro
Quando atingir esta consistência, adicione os queijos já picados e o requeijão
Continue mexendo até que os queijos derretam, então desligue o fogo
Adicione a outra colher de margarina e sirva."""


    
    @re_botcmd(pattern=r"^[Rr]isoto de [Pp]almito.*$")
    def Risoto_de_palmito(self, msg, match):
        self.send_stream_request(msg.frm, open('risotodepalmito.jpg', 'rb'), name='risotodepalmito.jpg', stream_type='photo')
        yield """Ingredientes
2 xícaras de arroz
250 g de creme de leite
½ cebola ralada
3 colheres de manteiga
1 xícara de palmito
1 colher (sopa) de salsa picadinha
4 colheres (sopa) de queijo parmesão ralado
½ xícara de vinho branco seco
1 cubo de caldo de galinha dissolvido em 4 xícaras de água quente
1 xícara de mussarela ralada"""
        
        yield """

Modo de preparo"""

        yield"""
Numa panela grossa, aqueça 2 colheres de manteiga, refogue a cebola até ficar transparente
Junte o arroz, refogue rapidamente, coloque o vinho, mexa até evaporar
Adicione metade do caldo e mexa
Deixe cozinhar por uns 5 minutos, adicione o restante do caldo e mexa novamente, deixe reduzir o caldo
Desligue o fogo ou abaixe bem, junte o palmito, o creme de leite, o restante de manteiga e o queijo
Misture tudo, polvilhe com a salsa e sirva em seguida."""

         

#---------------------------------------------------------------------FAROFAS------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    @re_botcmd(pattern=r"^[Ff]arofas.*$")    
    def Farofas(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD
\Farofa de cenoura e milho
\Farofa de bacon
\Farofa de linguiça
\Farofa verde com ovos"""

        
    
    @re_botcmd(pattern=r"^[Ff]arofa de [Cc]enoura e [Mm]ilho.*$")
    def Farofa_de_cenoura_e_milho(self, msg, match):
        self.send_stream_request(msg.frm, open('farofadecenouraemilho.jpg', 'rb'), name='farofadecenouraemilho.jpg', stream_type='photo')
        yield """Ingredientes
150g de bacon em cubos
3 colheres (sopa) de manteiga
1 xícara (chá) de cenoura ralada
1 lata de milho verde escorrido
1/2 xícara (chá) de azeitona verde fatiada
Sal, pimenta-do-reino e cheiro-verde picado a gosto
2 e 1/2 xícaras (chá) de farinha de milho
2 ovos cozidos picados"""
        
        yield"""
Modo de preparo"""

        yield"""
Aqueça uma panela, em fogo médio, e frite o bacon na própria gordura até começar a dourar. Junte a manteiga, a cenoura e refogue por 2 minutos. 
Despeje o milho, a azeitona, sal, pimenta e refogue por 2 minutos. 
Adicione a farinha e misture. 
Desligue, misture o ovo, cheiro-verde e transfira para uma travessa. 
Sirva."""

    
    @re_botcmd(pattern=r"^[Ff]arofa de [Bb]acon.*$")
    def Farofa_de_bacon(self, msg, match):
        self.send_stream_request(msg.frm, open('farofadebacon.jpg', 'rb'), name='farofadebacon.jpg', stream_type='photo')
        yield """Ingredientes
2 xícaras (chá) de bacon picado
2 colheres (sopa) de manteiga
1 cenoura ralada
150g de vagem picada
1 lata de milho verde escorrido
1 lata de ervilha escorrida
3 xícaras (chá) de farinha de milho
Sal e pimenta-do-reino a gosto"""
        
        yield"""
 
Modo de preparo"""

        yield """
Aqueça uma panela com o bacon e a manteiga, em fogo médio, e frite até dourar. 
Adicione a cenoura, a vagem, o milho, a ervilha e refogue por alguns minutos. 
Acrescente a farinha de milho e misture até ficar homogêneo. 
Desligue, tempere com sal, pimenta e sirva em seguida."""

    @re_botcmd(pattern=r"^[Ff]arofa de [Ll]ingui.*$")
    def Farofa_de_linguica(self, msg, match):
        self.send_stream_request(msg.frm, open('farofadelinguiça.jpg', 'rb'), name='farofadelinguiça.jpg', stream_type='photo')
        yield """Ingredientes
500g de linguiça de pernil picada
3 colheres (sopa) de azeite
2 cebolas em pétalas
1/2 xícara (chá) de salsa picada
1 e 1/2 xícara (chá) de farinha de mandioca
Sal e pimenta-do-reino a gosto"""
        
        yield """
Modo de preparo"""
   
        yield """
Em uma panela grande, em fogo médio, frite a linguiça no azeite. 
Quando estiver dourada, adicione a cebola e frite por mais 5 minutos. 
Misture com a salsa, a farinha de mandioca e tempere com sal e pimenta. 
Sirva em seguida."""

    
    @re_botcmd(pattern=r"^[Ff]arofa [Vv]erde com [Oo]vos.*$")
    def Farofa_verde_com_ovos(self, msg, match):
        self.send_stream_request(msg.frm, open('farofaverdecomovos.jpg', 'rb'), name='farofaverdecomovos.jpg', stream_type='photo')
        yield """Ingredientes
4 colheres (sopa) de manteiga
4 ovos batidos
2 colheres (chá) de sal
1/2 colheres (chá) de pimenta-do-reino
2 colheres (chá) de orégano
1/2 xícara (chá) de cebolinha picada
1/2 xícara (chá) de salsa picada
4 xícaras (chá) de farinha de rosca"""
        
        yield """

Modo de preparo"""

        yield """
Em uma panela, aqueça a manteiga em fogo médio, coloque os ovos, o sal, a pimenta, o orégano, a cebolinha e a salsa. 
Deixe firmar um pouco. 
Desmanche os ovos com uma colher de pau, adicione a farinha de rosca, misture rapidamente e sirva em seguida acompanhando assados e peixes."""
        
        
                
   
   

#--------------------------------------------------------------------------APERITIVOS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    
    @re_botcmd(pattern=r"^[Aa]peritivos.*$")
    def Aperitivos(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD
Bolinho de aipim
Bolinho de batata
Nuggets de frango
Guacamole
Banana frita temperada
Pipoca na panela
Biscoito de polvilho"""

    
    @re_botcmd(pattern=r"^[Bb]olinho de [Aa]ipim.*$")
    def Bolinho_de_aipim(self, msg, match):
        self.send_stream_request(msg.frm, open('bolinhodeaipim.jpg', 'rb'), name='bolinhodeaipim.jpg', stream_type='photo')
        yield """Ingredientes
1 kg de aipim cozido e amassado
2 ovos
1 colher de margarina
sal a gosto
200 g de queijo prato ou mussarela em cubinhos
farinha de rosca para empanar
óleo para fritar
papel-toalha"""
        
        yield """

Modo de preparo """

        yield """
Coloque em uma vasilha o aipim amassado, 1 ovo, a margarina e o sal, misture tudo muito bem
Faça bolinhas no tamanho de sua preferência, amasse a bolinha, coloque um cubinho de queijo e volte a enrolar
Passe as bolinhas no ovo que sobrou e empane na farinha de rosca
Frite em óleo bem quente até que doure
Em seguida, coloque os bolinhos em um prato forrado com papel-toalha para retirar o excesso de óleo
"""

    
    @re_botcmd(pattern=r"^[Bb]olinho de [Bb]atata.*$")
    def Bolinho_de_batata(self, msg, match):
        self.send_stream_request(msg.frm, open('bolinhodebatata.jpg', 'rb'), name='bolinhodebatata.jpg', stream_type='photo')
        yield """Ingredientes
5 unidades de batata
2 colheres (sopa) de farinha de trigo
2 unidades de ovo
salsinha a gosto
cebolinha verde a gosto
sal a gosto
1 colher (chá) de fermento químico em pó"""
        
        yield """

Modo de preparo"""

        yield """

Em uma bacia grande ralar as 5 batatas cruas. 
Misturar as 2 colheres de farinha de trigo, os 2 ovos inteiros, a salsa e cebolinha verde picadas, o sal e 1 colher de fermento até ficar uma massa homogênea.         
Com uma colher de sopa colocar uma quantidade da massa na frigideira e fritar com óleo não muito quente até ficarem douradinhos.             
Servir em porções."""


    
    @re_botcmd(pattern=r"^[Nn]uggets de [Ff]rango.*$")
    def Nuggets_de_frango(self, msg, match):
        self.send_stream_request(msg.frm, open('nuggetsdefrango.jpg', 'rb'), name='nuggetsdefrango.jpg', stream_type='photo')
        yield """Ingredientes
250g de frango moído
3 dentes de alho triturados
1 gema
suco de 1/2 limão
2 colheres (sopa) de salsinha verde picada
3 dentes de alho triturados
sal e pimenta do reino a gosto
1/2 colher (chá) de páprica doce
1 colher (sopa) de manjericão picado
Para empanar: 1 clara, farinha de trigo e farinha de rosca ou Panko"""
        
        yield """

Modo de preparo"""

        yield """
Corte o filé de frango em cubos.
No processador adicione o frango, o suco de limão, o alho, o sal, a pimenta do reino, a páprica doce e bata bem. 
Adicione  a salsinha, o manjericão, a gema do ovo (reserve a clara para usar depois) e bata.
Pegue porções de massa, faça uma bolinha, achate um pouquinho e modele o Nuggets, repita esse procedimento até finalizar a massa.
Para empanar passe primeiro na farinha de trigo, depois na clara e depois na farinha panko ou farinha de rosca."""
        
        yield """
Para preparar no FORNO"""

        yield """

Siga colocando cada bolinho em uma forma anti aderente, regue com azeite. 
Levo ao forno pré aquecido à 200º por 20 minutos, parando na metade do tempo para virar e regar com azeite."""
        yield """ 
Para FRITAR"""

        yield """
Em uma panela com óleo adicione os bolinhos. 
Deixe dourar de um lado e vire para dourar do outro. 
Siga colocando em papel toalha para tirar o excesso de gordura."""



    
    @re_botcmd(pattern=r"^[Gg]uacamole.*$")
    def Guacamole(self, msg, match):
        self.send_stream_request(msg.frm, open('guacamole.jpg', 'rb'), name='guacamole.jpg', stream_type='photo')
        yield """Ingredientes
1 abacate
1 tomate em cubinhos (sem semente)
suco de 1 limão
1 colher (chá) de pimenta dedo de moça picadinha ou molho de pimenta
2 colheres (sopa) de coentro picado
sal a gosto
1 colher (sopa) de cebola bem picadinha
1 colher (sopa) de azeite de oliva"""

        yield """

Modo de preparo"""

        yield """
Pique o abacate em cubos pequenos.
Em uma tigela misture o abacate com todos os ingredientes, utilizando um garfo. 
Sirva a seguir."""


    
    @re_botcmd(pattern=r"^[Bb]anana [Ff]rita [Tt]emperada.*$")
    def Banana_frita_temperada(self, msg, match):
        self.send_stream_request(msg.frm, open('bananafritaempanada.jpg', 'rb'), name='bananafritaempanada.jpg', stream_type='photo')
        yield """Ingredientes
4 bananas da terra
páprica doce a gosto
curry a gosto
sal a gosto
óleo para fritar"""
        
        yield """

Modo de preparo"""

        yield """

Retire as cascas das bananas e passe-as direto no mandolim ou ralador para cortar em rodelas uniformes.
Em uma frigideira com um pouco de óleo, doure do dois lados.
Siga colocando em cima de papel toalha para secar e tempere com sal, páprica e curry, misturando muito bem.
Coloque em potinhos e sirva a seguir."""


    
    @re_botcmd(pattern=r"^[Pp]ipoca na [Pp]anela.*$")
    def Pipoca_na_panela(self, msg, match):
        self.send_stream_request(msg.frm, open('pipocanapanela.jpg', 'rb'), name='pipocanapanela.jpg', stream_type='photo')
        yield """Ingredientes
1 xícara de milho para pipoca
2 colheres (sopa) de óleo
Sal ou açúcar a gosto"""
        
        yield """
Modo de preparo"""

        yield """
Em uma panela alta coloque os milhos, cubra com o óleo e misture.
Ligue o fogo alto e fique misturando sem parar.
Quando estourar a primeira pipoca tampe imediatamente, e deixe que os milhos sigam se estourando.
Dê uma chacoalhada na panela com cuidado e quando parar de estourar desligue o fogo.
Tempere com sal."""


    
    @re_botcmd(pattern=r"^[Bb]iscoito de [Pp]olvilho.*$")
    def Biscoito_de_polvilho(self, msg, match):
        self.send_stream_request(msg.frm, open('biscoitodepolvilho.jpg', 'rb'), name='biscoitodepolvilho.jpg', stream_type='photo')
        yield """Ingredientes
500g de polvilho azedo
1 xícara (chá) de leite
1 xícara (chá) de óleo
1 xícara (chá) de água morna
1 ovo
1 colher (sopa) de sal"""
        
        yield """

Modo de preparo"""

        yield """

Em uma tigela grande misture o polvilho com o sal.
Em uma panela coloque o leite e o óleo, quando levantar fervura desligue o fogo, e adicione imediatamente na tigela com o polvilho misturando sem parar até obter uma massa homogênea.
Acrescente o ovo levemente batido e misture, aos poucos siga adicionando a água morna e mexendo rapidamente com uma colher ou batedor.
Transfira a massa para uma batedeira e bata até atingir consistência cremosa firme.
Após, coloque a massa em um saco de confeitar e faça formatos conforme desejar, colocando diretamente em uma forma untada com manteiga e polvilhada com farinha de trigo.
Leve ao forno pré-aquecido a 180° por aproximadamente 20 – 25 minutos, ou até que estejam levemente dourados."""


        
        
        
        
        
        
#------------------------------------------------------------------------------BOLOS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    
    
    
    @re_botcmd(pattern=r"^[Bb]olos$")
    def Bolos(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD 
\Bolo de Cenoura
\Bolinho de chuva
\Bolo de Chocolate
\Bolo de milho
"""


    
    @re_botcmd(pattern=r"^[Bb]olo de [Cc]enoura.*$")
    def Bolo_de_Cenoura(self, msg, match):
        self.send_stream_request(msg.frm, open('bolodecenoura.jpg', 'rb'), name='bolodecenoura.jpg', stream_type='photo')
        yield """Ingredientes
1 xícara de cenoura picada
3 ovos
1 xícara de açúcar
1 xícara (chá) de óleo
1 colher (sopa) de fermento em pó
1 e 1/2 xícara de farinha de trigo
1 lata de leite condensado
4 colheres (sopa) de chocolate em pó
1 colher (sopa) de margarina"""
         

        yield """
Modo de preparo """
        
        yield """

Junte no liquidificador a cenoura, os ovos, o açúcar e o óleo e bata por uns 5 minutos
Despeje este conteúdo em um recipiente, acrescente a farinha e o fermento e misture bem
Unte com óleo uma forma de buraco central
Leve ao forno em temperatura baixa, por mais ou menos, 40 minutos
Para fazer a cobertura, utilize 1 lata de leite condensado, junte 4 colheres de sopa de chocolate em pó e uma colher de margarina
Quando engrossar (mas um pouco antes de começar a aparecer o fundo da panela) está pronto.
         """

   
    
    @re_botcmd(pattern=r"^[Bb]olinho de [Cc]huva.*$")
    def Bolinho_de_chuva(self, msg, match):
        self.send_stream_request(msg.frm, open('bolodechuva.jpg', 'rb'), name='bolodechuva.jpg', stream_type='photo')

        yield """Ingredientes
3 xícaras de farinha de trigo
3 ovos ligeiramente batidos
6 colheres de açúcar
1/2 xícara de leite
1 pitada de sal
1 colher de sopa de fermento em pó
Açúcar e canela para polvilhar"""
        
 
        yield"""
 Modo de preparo"""

        yield """

Misture todos os ingredientes numa vasilha
Frite as colheradas em óleo quente
Polvilhe açúcar e canela
        """


    
    @re_botcmd(pattern=r"^[Bb]olo de [Cc]hocolate.*$")
    def Bolo_de_Chocolate(self, msg, match):
        self.send_stream_request(msg.frm, open('bolo.jpg', 'rb'), name='bolo.jpg', stream_type='photo')
        yield """ Ingredientes
Massa
1 xícara (chá) de achocolado ou chocolate em pó
1 xícara (chá) de açúcar
2 xícaras (chá) de trigo peneirado
1 xícara (chá) de óleo
1 xícara (chá) de leite
2 ovos
1 colher (sopa) de fermento em pó"""
        
        yield"""

Calda"""
        yield """
1 colher (sopa) de margarina
3 colheres (sopa) de achocolatado ou chocolate em pó
3 colheres de açúcar
1 xícara (chá) de leite"""
            

        yield """
Modo de preparo"""

        yield """
Massa e trigo 
Bater todos os ingredientes no liquidificador
Assar por 35 minutos."""
        
        yield """
Calda"""

        yield """
Em uma panela coloque no fogo
Untar uma forma com margarina médio a margarina para derreter
Assim que derreter coloque o açúcar e em seguida o achocolatado, por último acrescente o leite
Mexa de vez em quando para não gastar, espere engrossar um pouco e despeje ainda quente no bolo
            """

       
    
    @re_botcmd(pattern=r"^[Bb]olo de [Mm]ilho.*$")
    def Bolo_de_milho(self, msg, match):
        self.send_stream_request(msg.frm, open('bolodemilho.jpg', 'rb'), name='bolodemilho.jpg', stream_type='photo')

        
        yield """Ingredientes
1 lata de milho verde (descarte a água)
1/2 xícara (chá) de leite
3/4 xícara (chá) de óleo
3 ovos
1 e 1/2 xícara (chá) de açúcar
2 xícaras (chá) de farinha de trigo
1/2 xícara (chá) de amido de milho
1 colher (sopa) de fermento em pó
Para finalizar: Açúcar e Canela em pó"""

        yield """
Modo de Preparo"""
 
        yield """

No liquidificador bata bem o leite, o óleo, o milho, o açúcar e os ovos.
Em uma tigela passe pela peneira a farinha de trigo e o amido de milho.
Despeje o conteúdo do liquidificador. Misture.
Despeje em uma forma de furo central alta (20cm) untada e enfarinhada.
Leve ao forno preaquecido a 180° por aproximadamente 40 minutos.
Após, espere esfriar para desenformar e polvilhe açúcar com canela em pó.        """

    


#---------------------------------------------------------------------------PUDINS-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#   
   
    
    @re_botcmd(pattern=r"^[Pp]udins.*$")
    def Pudins(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD 
\Pudim de chocolate
\Pudim de leite
\Quindim """

   
    
    @re_botcmd(pattern=r"^[Pp]udim de [Cc]hocolate.*$")
    def Pudim_de_chocolate(self, msg, match):
        self.send_stream_request(msg.frm, open('pudimdechocolate.jpg', 'rb'), name='pudimdechocolate.jpg', stream_type='photo')

        yield """Ingredientes
1 lata de creme de leite
1 lata de leite condensado
1 copo cheio de leite (copo americano)
1/2 xícara chá de chocolate em pó
1 pacote de gelatina incolor
1 pacote de chocolate granulado"""
         

        yield"""
Modo de preparo"""

        yield """
No liquidificador adicione o leite condensado, o creme de leite, o leite e o chocolate em pó
Bata bem, em seguida acrescente a gelatina dissolvida conforme as instruções da embalagem, bata somente para misturar
Unte com pouco óleo uma fôrma para pudim, depois enxágue a fôrma para tirar o excesso de óleo, despeje o líquido batido e leve para gelar por 10 horas
Desenforme na hora de servir e salpique o granulado por cima.
         """


    
    @re_botcmd(pattern=r"^[Pp]udim de [Ll]eite.*$")
    def Pudim_de_leite(self, msg, match):
        self.send_stream_request(msg.frm, open('pudimdeleite.jpg', 'rb'), name='pudimdeleite.jpg', stream_type='photo')

        yield """Ingredientes

1 lata de leite condensado
2 latas de leite (medida da lata de leite condensado)
3 ovos"""
        
        yield"""

Calda
1 xícara (chá) de açúcar"""
        
        yield"""
Modo de preparo"""

        yield"""
Calda"""

        yield """

Em uma panela de fundo largo, derreta o açúcar até ficar dourado
Junte 1/2 xícara (chá) de água quente e mexa com uma colher
Deixe ferver até dissolver os torrões de açúcar e a calda engrossar
Forre com a calda uma forma com furo central (19 cm de diâmetro) e reserve"""
         

        yield """
Pudim"""


        yield """
Bata todos os ingredientes do pudim no liquidificador e despeje na forma reservada
Asse em banho-maria, em forno médio (180º C), por cerca de 1 hora e 30 minutos
Depois de frio, leve para gelar por cerca de 6 horas
Desenforme e sirva a seguir
         """


    
    @re_botcmd(pattern=r"^[Qq]uindim.*$")
    def Quindim(self, msg, match):
        self.send_stream_request(msg.frm, open('quindim.jpg', 'rb'), name='quindim.jpg', stream_type='photo')
       
        yield """Ingredientes
12 gemas peneiradas
200g de açúcar refinado
50g de coco flocado ou coco ralado fresco
1 colher (sopa) de manteiga derretida
200ml de leite de coco"""
        
        yield """

Modo de preparo"""

        yield """
Em uma tigela misture o açúcar com o coco e a manteiga.
Adicione o leite de coco e a tigela de gemas, e misture bem até ficar homogêneo.
Deixe descansar 30 minutos coberto com filme plástico.
Unte as forminhas com manteiga e polvilhe açúcar refinado, e preencha com a mistura.
Pegue uma forma grande e encha com água quente para fazer o banho-maria.
Leve ao forno médio pré-aquecido por aproximadamente 40 – 50 minutos ou até que esteja levemente dourado.
Desenforme frio, com cuidado passando a ponta de uma faca em volta para que desgrude com mais facilidade.
Mantenha na geladeira até o momento de servir.
        """
   
   
   
#-----------------------------------------------------------------------MOUSSES----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#   
   
   
    
    @re_botcmd(pattern=r"^[Mm]ousses.*$")
    def Mousses(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD
\Mousse de morango 
\Mousse de limão
\Mousse de maracujá
\Mousse fácil de chocolate """


    
    @re_botcmd(pattern=r"^[Mm]ousse de [Mm]orango.*$")
    def Mousse_de_morango(self, msg, match):    
        self.send_stream_request(msg.frm, open('moussedemorango.jpg', 'rb'), name='moussedemorango.jpg', stream_type='photo')
        yield """Ingredientes
1 caixa de morangos
1 lata de leite condensado
1 lata de creme de leite
1 gelatina de morango
1 gelatina sem sabor
500ml de água
3 colheres de sopa de açúcar (a gosto)"""
        
        yield"""

Modo de preparo""" 


        yield """
Ferva a água, apague o fogo, jogue as 2 gelatinas dentro, mexa até dissolver
Lave o morango e tire as folhinhas
Coloque todos os ingredientes no liquidificador e bata por 3 minutos
Despeje em uma forma de vidro, leve p/ geladeira por 3 horas."""

     
    

    @re_botcmd(pattern=r"^[Mm]ousse de [Ll]im.*$")
    def Mousse_de_limao(self, msg, match):
        self.send_stream_request(msg.frm, open('moussedelimao.jpg', 'rb'), name='moussedelimao.jpg', stream_type='photo')
        yield """Ingredientes
1 lata de leite condensado
1 caixinha de creme de leite
½ xícara de suco de limão puro
Raspas de limão para salpicar"""
        

        yield """
Modo de preparo"""

        yield """
No liquidificador bata bem o creme de leite com o leite condensado.
Após, adicione o suco de limão e bata novamente.
Disponha em taças individuais ou em uma travessa média.
Salpique as raspas de limão.
Leve a geladeira por no mínimo 4 horas e sirva a seguir."""


    
    @re_botcmd(pattern=r"^[Mm]ousse de [Mm]aracu.*$")
    def Mousse_de_maracuja(self, msg, match):
        self.send_stream_request(msg.frm, open('moussedemaracuja.jpg', 'rb'), name='moussedemaracuja.jpg', stream_type='photo')
        yield """Ingredientes
2 caixas de gelatina de maracujá
2 xícaras de água quente
1/2 xícara de suco de maracujá
2 xícaras de leite de vaca
1 lata de leite condensado
1 lata de creme de leite sem soro"""
    
        yield """
Modo de preparo"""

        yield """
Prepare a gelatina com a água quente
Depois é só bater todos os ingredientes no liquidificador e colocar numa travessa para gelar."""


    
    @re_botcmd(pattern=r"^[Mm]ousse [Ff].*cil de [Cc]hocolate.*$")
    def Mousse_facil_de_chocolate(self, msg, match):
        self.send_stream_request(msg.frm, open('moussefacildechocolate.jpg', 'rb'), name='moussefacildechocolate.jpg', stream_type='photo')
        yield """Ingredientes
200g de chocolate meio amargo
3 claras
4 colheres (sopa) de açúcar
1 lata de creme de leite
Para decorar: chantilly, cereja e folhas de hortelã"""
        
        yield """
Modo de preparo"""


        yield """
Derreta o chocolate e adicione o creme de leite. 
Misture muito bem. 
Reserve.
Em uma panela adicione as claras com o açúcar, em fogo baixo, mexendo sem parar por aproximadamente 3 minutos (cuidado para as claras não cozinharem).
Desligue o fogo e adicione na tigela da batedeira e bata muito bem até dobrar de volume.
Delicadamente adicione o creme de chocolate.
Despeje direto nas taças de servir, e decore com chantilly, cereja e hortelã.
Leve a geladeira por aproximadamente 3 horas. """







#-----------------------------------------------------------------------------DOCES FESTIVOS---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


    
    @re_botcmd(pattern=r"^[Dd]oces [Ff]estivos.*$")
    def Doces_Festivos(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD
\Brigadeiro
\Docinho de coco queimado
\Brigadeiro gourmet de nutella
\Pé_de_moleque
\Beijinho de coco """


    
    @re_botcmd(pattern=r"^[Bb]rigadeiro.*$")
    def Brigadeiro(self, msg, match):
        self.send_stream_request(msg.frm, open('brigadeiro.jpg', 'rb'), name='brigadeiro.jpg', stream_type='photo')
        yield """Ingredientes
1 caixa de leite condensado
1 colher (sopa) de margarina sem sal
7 colheres (sopa) de achocolatado ou 4 colheres (sopa) de chocolate em pó
chocolate granulado"""
        
        yield """ 
Modo de preparo"""
        
        yield """
Em uma panela funda, acrescente o leite condensado, a margarina e o chocolate em pó
Cozinhe em fogo médio e mexa até que o brigadeiro comece a desgrudar da panela
Deixe esfriar e faça pequenas bolas com a mão passando a massa no chocolate granulado. """

    
    @re_botcmd(pattern=r"^[Dd]ocinho de [Cc]oco [Qq]ueimado.*$")
    def Docinho_de_coco_queimado(self, msg, match):
        self.send_stream_request(msg.frm, open('docinhodecocoqueimado.jpg', 'rb'), name='docinhodecocoqueimado.jpg', stream_type='photo')
        yield """Ingredientes
1 lata de doce de leite
1 colher (sopa) manteiga sem sal
120ml de leite de coco
1 xícara (chá) de coco queimado
coco queimado para decorar"""

        yield """

Modo de preparo"""

        yield """
Em uma panela coloque o doce de leite, a manteiga, o leite de coco e o coco queimado.
Deixe apurar, sem para de mexer, até soltar do fundo da panela.
Despeje o doce em um prato untado com manteiga e espere esfriar para começar a enrolar.
Com as mãos untadas de manteiga faça bolinhas e passe pelo coco queimado."""


    
    @re_botcmd(pattern=r"^[Bb]rigadeiro [Gg]oumert de [Nn]utella.*$")
    def Brigadeiro_gourmet_de_nutella(self, msg, match):
        self.send_stream_request(msg.frm, open('dgnutella.jpg', 'rb'), name='dgnutella.jpg', stream_type='photo')
        yield """Ingredientes
2 latas de leite condensado
1 colher (sopa) de manteiga sem sal
200g de chocolate ao leite belga
150g de chocolate meio amargo belga
250g de nutella
1 colher (sopa) de glucose
confeitos para decorar"""
        
        yield """
Modo de preparo"""
  
        yield """
Pique os chocolates. 
Reserve.
Na panela adicione todos os ingredientes, misture sem parar, até soltar do fundo da panela, como um brigadeiro tradicional.
Após, despeje o brigadeiro em um prato untado com manteiga de deixe esfriar totalmente para começar a fazer as bolinhas.
Comece fazendo as bolinhas com as mãos untadas com manteiga e passe pelos confeitos de sua preferência.  """


    
    @re_botcmd(pattern=r"^[Pp].* de [Mm]oleque.*$")
    def Pe_de_moleque(self, msg, match):
        self.send_stream_request(msg.frm, open('pedemoleque.jpg', 'rb'), name='pedemoleque.jpg', stream_type='photo')
        yield """Ingredientes
2 xícaras (chá) de amendoim sem pele e torrado
1 xícara (chá) de açúcar cristal
1 lata de leite condensado
2 colheres (sopa) de glucose de milho
1/2 colher (chá) de bicarbonato de sódio"""
        
        yield """

Modo de preparo"""

        yield """

Em uma panela coloque o açúcar, a glucose e o amendoim. 
Deixe derreter todo açúcar e caramelizar.
Na sequência adicione o leite condensado. 
Misture bem até começar a soltar do fundo da panela.
Nesse momento adicione o bicarbonato (Ele vai espumar, não se assuste!), siga misturando até baixar e soltar do fundo da panela (como um ponto de brigadeiro).
Despeje a massa em uma mármore untado com manteiga, e tente acomodar num formato quadrado. 
Deixe amornar um pouquinho e corte com uma faca untada com manteiga em quadradinhos (se esfriar totalmente ficará duro e você não conseguirá cortar).
Depois de frio guarde em potinhos."""


    
    @re_botcmd(pattern=r"^[Bb]eijinho de [Cc]oco.*$")
    def Beijinho_de_coco(self, msg, match):
        self.send_stream_request(msg.frm, open('beijinho.jpg', 'rb'), name='beijinho.jpg', stream_type='photo')
        yield """Ingredientes
1 lata de leite condensado
1 colher (sopa) de manteiga sem sal
100g de coco desidratado em flocos (ralado grosso)
Coco ralado para empanar"""

        yield """
Modo de preparo"""

        yield """

Em uma panela coloque o leite condensado e a manteiga e misture até derreter a manteiga.
Após adicione o coco e misture bem.
Siga misturando em fogo baixo até que solte do fundo da panela.
Em um prato untado com manteiga coloque a massa e espere esfriar. 
Reserve.
Coloque o coco ralado em um prato fundo para empanar.
Quando frio unte as suas mãos com manteiga e faça as bolinhas, enrolando bem e passando pelo coco para empanar.
Siga colocando nas forminhas de sua preferência."""
   
   
   
   
#---------------------------------------------------------------------------TORTAS-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#   
   
    
    @re_botcmd(pattern=r"^[Tt]ortas.*$")
    def Tortas(self, msg, match):
        yield """Eii, falta pouquinho… só falta escolher uma dessas receitas XD
\Cheesecake de morango
\Torta de maçã
\Torta de sorvete com frutas vermelhas 
\Torta de mousse de chocolate
\Torta de ricota com goiabada"""


    
    @re_botcmd(pattern=r"^[Cc]heesecake de [Mm]orango.*$")
    def Cheesecake_de_morango(self, msg, match):
        self.send_stream_request(msg.frm, open('cheesecakedemorango.jpg', 'rb'), name='cheesecakedemorango.jpg', stream_type='photo')
        yield """Ingredientes"""

        yield """
Base"""

        yield """

100g de biscoito de leite ou maizena
40g de manteiga derretida"""
    
        yield """
Creme"""

        yield"""
150g de cream cheese
180g de creme de leite fresco
suco de 1/2 limão
80g de açúcar
1 colher (sopa) de gelatina em pó sem sabor (6g) + 2 colheres (sopa)de água"""
        
        yield """
Cobertura"""

        yield """

1 pacote de gelatina de morango (30g)
125ml de água quente
125ml de água fria
1 caixa de morangos cortados ao meio"""
        
        yield """
Modo de preparo"""

        yield """
Para a base"""

        yield """
Bata os biscoitos no processador. 
Acrescente a manteiga derretida e bata novamente. 
Despeje na forma ( ARO 16 – já untada com manteiga) e alise com uma colher. 
Leve ao forno preaquecido a 200º por aproximadamente 10 minutos. 
Após, espere esfriar uma utilizar."""
        
        yield """
Para o creme"""

        yield """
Na batedeira adicione o creme de leite fresco (que deve ficar 20 minutos no freezer antes para bater em ponto de Chantilly). 
Quando chegar no ponto transfira e reserve em um prato.
Ainda na batedeira adicione o cream cheese, o açúcar, o suco de limão e bata bem. 
Hidrate a gelatina adicionando água e aquecendo no microondas conforme as instruções da embalagem. 
Adicione a gelatina ao creme e bata bem. 
Desligue a batedeira e acrescente o Chantilly reservando misturando delicadamente.
Pegue a forma com a base de biscoitos e despeje o creme. 
Cubra com filme plástico e leve à geladeira até firmar, aproximadamente 2 horas.
Em uma tigela despeje a gelatina de morango, adicione a água quente, misture. acrescente a água gelada, misture. 
Leve à geladeira apenas para começar a enrijecer, por aproximadamente 30 minutos.
Retire a cheesecake da geladeira. 
Decore com morangos cortados ao meio e despeje a gelatina de morango. 
Leve à geladeira por 4 horas, ou até que esteja completamente firme.
Na hora de servir decore com morangos."""

    
    @re_botcmd(pattern=r"^[Tt]orta de [Mm]a.*$")
    def Torta_de_maca(self, msg, match):
        self.send_stream_request(msg.frm, open('tortademaça.jpg', 'rb'), name='tortademaça.jpg', stream_type='photo')
        yield """Ingredientes
           
Massa
150g de manteiga gelada
3/4 xícara (chá) de açúcar
1 ovo
3 xícaras (chá) de farinha de trigo
1/2 colher (chá) de fermento em pó
pitada de sal
1/2 colher (chá) de raspas de limão
2 colheres (sopa) de leite"""

        yield"""
Recheio"""

        yield"""
6 maçãs
suco de 1/2 limão
2 colheres (sopa) de manteiga
1/2 colher (chá) de canela em pó
1/2 xícara (chá) de açúcar
1/2 xícara (chá) de suco de laranja
1 colher (sopa) de amido de milho"""

        yield"""
Finalização"""

        yield """
1 gema e açúcar cristal
Modo de preparo
Para a massa
Em uma tigela adicione os secos ( farinha, fermento, sal, açúcar) e misture com a manteiga, utilizando as pontinhas dos dedos até formar uma farofa úmida. 
Acrescente o ovo (já batido com as raspas de limão), e o leite. Misture e forme uma massa homogênea. (essa massa não deve ser sovada)
Embrulhe a massa com filme plástico e leve a geladeira por 30 minutos."""
                
        yield"""
Enquanto isso prepare o recheio"""

        yield""" 
Descasque as maçãs e corte em cubinhos (para que não escureçam enquanto corta esprema o suco de limão).
E uma panela adicione a manteiga e deixe derreter, acrescente o açúcar, a canela e a maçã.
Misture, tampe e deixe por 5 minutos.
Dissolva o amido no suco de laranja e despeje na panela.
Misture e deixe apurar alguns instantes. Desligue o fogo e reserve.
Retire a massa da geladeira, e abra com um rolo entre duas folhas de papel manteiga (reservando parte dela para finalização). 
Coloque direto em uma forma untada com manteiga, formando a base da torta . 
Faça furos (usando um garfo) por toda a superfície da massa, leve a geladeira por 20 minutos. 
Após leve ao forno pré aquecido a 180° por 8 minutos, apenas para pré assar.
Retire do forno e despeje o recheio (que deve estar frio). Abra o restante da maça e faça tiras.
Siga decorando a torta, com as sobrinhas da massa faça bolinhas e coloque em cima para decorar.
Pincele a gema batida em toda superfície e salpique açúcar cristal. 
Leva ao forno pré aquecido a 180° por aproximadamente 30 minutos ou até dourar."""

    
    @re_botcmd(pattern=r"^[Tt]orta de [Ss]orvete com [Ff]rutas [Vv]ermelhas.*$")
    def Torta_de_sorvete_com_frutas_vermelhas(self, msg, match):
        self.send_stream_request(msg.frm, open('tortasorvete.jpg', 'rb'), name='tortasorvete.jpg', stream_type='photo')
        yield """Ingredientes
2 xícaras (chá) de morangos fatiados
2 kiwis em cubinhos
2 litros de sorvete de creme"""

        yield """
Calda de morango"""

        yield """
1 xícara (chá) de açúcar
2 xícaras (chá) de morangos picados"""
        
        yield """
Modo de preparo"""

        yield"""
Corte os morangos em fatias e os kiwis em cubinhos.
Pegue uma forma redonda de aro removível e forre com filme plástico.
Faça uma camada de frutas, em cima adicione todo o sorvete e por cima coloque mais frutas.
Feche com filme plástico e leve ao freezer por aproximadamente 3 horas, ou até que esteja bem firme.
Enquanto isso para a calda de morango misture os ingredientes e leve ao microondas por 3 minutos, misturando na metade do tempo. 
Deixe esfriar para ser utilizado.
Depois, desenforme a torta sorvete e regue com a calda
Ingredientes
2 xícaras (chá) de morangos fatiados
2 kiwis em cubinhos
2 litros de sorvete de creme"""
        
        yield"""
Calda de morango"""

        yield"""
1 xícara (chá) de açúcar
2 xícaras (chá) de morangos picados"""
         
        yield """
Modo de preparo"""

        yield"""
Corte os morangos em fatias e os kiwis em cubinhos.
Pegue uma forma redonda de aro removível e forre com filme plástico.
Faça uma camada de frutas, em cima adicione todo o sorvete e por cima coloque mais frutas.
Feche com filme plástico e leve ao freezer por aproximadamente 3 horas, ou até que esteja bem firme.
Enquanto isso para a calda de morango misture os ingredientes e leve ao microondas por 3 minutos, misturando na metade do tempo. 
Deixe esfriar para ser utilizado.
Depois, desenforme a torta sorvete e regue com a calda
"""

    
    @re_botcmd(pattern=r"^[Tt]orta de [Mm]ousse de [Cc]hocolate.*$")
    def Torta_de_mousse_de_chocolate(self, msg, match):
        self.send_stream_request(msg.frm, open('tortamouseedechocolate.jpg', 'rb'), name='tortamouseedechocolate.jpg', stream_type='photo')
        yield """Ingredientes

100g de biscoito (tipo maizena)
50g de manteiga sem sal
6 avelãs"""

        yield"""
Mousse Meio Amargo e Ao leite"""

        yield"""
200g de chocolate meio amargo Perugina
200g de chocolate ao leite Perugina
200g de creme de leite
2 colheres (sopa) de gelatina em pó ( total 12g) + 6 colheres (sopa) de água
2 claras
1/3 xícara (chá) de açúcar
20 unidades de Bacio Perugina"""
       
        yield"""
Modo de preparo"""

        yield"""
Para a Base"""

        yield """
No processador bata bem os biscoitos com as avelãs até formar uma farofinha. 
Acrescente a manteiga derretida e bata novamente até formar uma farofinha úmida. 
Em um forma de fundo removível ( ARO 16) untada com manteiga faça uma camada com essa farofa, fazendo pressão com as costas de uma colher em toda superfície. 
Leve ao forno preaquecido a 180°, por aproximadamente 12 – 15 minutos.
Deixe esfriar para continuar."""

        yield """
Para as mousses"""


        yield """
Pegue duas tigelas. Em uma coloque o chocolate ao leite picado e na outra o chocolate meio amargo picado. 
Derreta em banho-maria ou leve ao microondas para derreter, parando a cada 30 segundos e mexendo, até que esteja completamente derretido. 
Acrescente metade do creme de leite em cada chocolate e misture.
Em uma tigelinha hidrate a gelatina incolor com água e aqueça no microondas ou em banho maria (conforme as instruções da embalagem). 
Divida em duas partes, e adicione metade em cada tigela com o chocolate e misture bem.
Em uma panela acrescente as claras, o açúcar e misture.
Aqueça em fogo bem baixinho, até que os grãos de açúcar estejam dissolvidos (aproximadamente 2 – 3 minutos). L
eve imediatamente a batedeira e bata até ficar fofo e firme.
Divida em duas partes e adicione metade em cada tigela com o chocolate e misture delicadamente."""
                 
        yield"""
Montagem"""

        yield"""
Pegue a forma com a base de biscoito e despeje a mousse de chocolate meio amargo.
Leve ao freezer por 20 minutos. 
Após, acrescente a mousse ao leite e leve à geladeira por aproximadamente 4 horas, ou se preferir prepare no dia anterior.
Na hora de servir coloque em cima vários Baci, e se desejar dar um toque especial prepare uma caldinha de açúcar (com 1/2 xícara de açúcar e 1/4 xícara de água), e despeje fazendo fios em cima da torta."""

    
    @re_botcmd(pattern=r"^[Tt]orta de [Rr]icota com [Gg]oiabada.*$")
    def Torta_de_ricota_com_goiabada(self, msg, match):
        self.send_stream_request(msg.frm, open('tortadericotacomgoiabada.jpg', 'rb'), name='tortadericotacomgoiabada.jpg', stream_type='photo')
        yield """Ingredientes
500g de ricota fresca
1 lata de leite condensado
3 colheres (sopa) de amido de milho
2 colheres (sopa) de açúcar
1 xícara (chá) de leite integral
4 ovos
pitada de sal
raspas de 1 limão
200g de goiabada em cubinhos + 1 colher (sopa) de amido"""

        yield"""
Cobertura"""

        yield """
150g de goiabada cortada
Aproximadamente 4 colheres (sopa) de água"""
            
        yield """    
Modo de preparo"""

        yield """
Em uma tigela misture a goiabada em cubinhos com 1 colher de amido de milho. 
Envolva os cubinhos no amido e reserve.
No liquidificador bata o leite condensado, as gemas, o amido de milho, a ricota, o leite e o açúcar. 
Reserve.
Na batedeira bata as claras em neve com uma pitada de sal até chegar ao ponto de neve.
Despeje a mistura do liquidificador nas claras, adicione as raspas de limão e misture com uma espátula delicadamente. 
Por último acrescente a goiabadaem cubinhos e misture novamente.
Em uma forma redonda ( aro 28cm) untada com manteiga despeje a massa.
Leve ao forno preaquecido a 180° por aproximadamente 40 minutos."""
    
        yield"""
Enquanto isso prepare a cobertura Em uma tigela com a goiabada picada acrescente a água. 
Leve ao microondas parando de vez em quando e mexendo até derreter completamente. 
Se necessário acrescente um pouco mais de água, até que a goiabada esteja cremosa.
Retire a torta do forno, espere esfriar alguns minutos e desenforme.
Basta despejar a cobertura de goiabada cremosa e está pronto!
"""




