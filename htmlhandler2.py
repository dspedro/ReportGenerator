
import json
import jmespath

def html (inc,dic):
  db = open("db/r/"+str(inc)+".json","r")
  dbj = json.load(db)
  print(dbj)
  f = open("html/"+str(inc)+".html","w")
	f.write('''
         <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
         <html>
        <head>

  
  <meta http-equiv="content-type" content="text/html; charset=ISO-8859-1">

  
  <title>Report</title>
</head>

<body>

<br>

<table style="width: 1046px; height: 1331px; text-align: left; margin-left: auto; margin-right: auto;" border="0" cellpadding="2" cellspacing="2">

  <tbody>

    <tr>

      <td style="text-align: center; width: 980px;">
      
      <table style="text-align: left; width: 100%; height: 136px;" border="1" cellpadding="2" cellspacing="2">

        <tbody>

          <tr>

            <td style="width: 15%; text-align: center;"><img style="width: 134px; height: 124px;" alt="Logo" src="img/logo.JPG"></td>

            <td style="text-align: center;">COMPROVANTE DE
PRESTA&Ccedil;&Atilde;O DE SERVI&Ccedil;O<br>

PARDAL AVIA&Ccedil;&Atilde;O AGR&Iacute;COLA LTDA<br>

FONE: (14) 3324-5715 e (14) 99706-8324<br>

Av. Sidney Marcondi 441 - Jd Santos Dumont - Ourinhos/SP</td>

            <td style="width: 25%; text-align: center;"><span style="font-weight: bold;">RELAT&Oacute;RIO OPERACIONAL<small><small><small><small><small><small><small><small><br>

            <br>

            </small></small></small></small></small></small></small></small><big><span style="color: rgb(255, 0, 0);">N&deg; &nbsp;'''+str(inc)+'''<small><small><small><small><small><br>

            <br>

            </small></small></small></small></small><small><small><span style="color: rgb(0, 0, 0);">Registro MAPA: &nbsp;80137-2</span></small></small></span></big></span></td>

          </tr>

        
        </tbody>
      
      </table>

      
      <table style="text-align: left; width: 100%; height: 144px;" border="1" cellpadding="2" cellspacing="2">

        <tbody>

          <tr>

            <td style="width: 15%; text-align: left;">Contratante:</td>
            <td>'''+contratante+'''</td>

          </tr>

          <tr>

            <td>Propriedade:</td>

            <td></td>

          </tr>

          <tr>

            <td>Localiza&ccedil;&atilde;o:</td>

            <td></td>

          </tr>

          <tr>

            <td>Munic&iacute;pio:</td>

            <td></td>

          </tr>

          <tr>

            <td>CNPJ/CPF:</td>

            <td></td>

          </tr>

        
        </tbody>
      
      </table>

      
      <table style="text-align: left; width: 100%; height: 116px;" border="1" cellpadding="2" cellspacing="2">

        <tbody>

          <tr>

            <td style="width: 20%;"><span style="font-weight: bold;">Tipo de servi&ccedil;o</span></td>

            <td style="width: 16%; text-align: center;"><span style="font-weight: bold;">Produto</span></td>

            <td style="width: 16%; text-align: center;"><span style="font-weight: bold;">Formula&ccedil;&atilde;o</span></td>

            <td style="width: 16%; text-align: center;"><span style="font-weight: bold;">Dosagem</span></td>

            <td style="width: 16%; text-align: center;"><span style="font-weight: bold;">Classe Toxicol&oacute;gica</span></td>

            <td style="width: 16%; text-align: center;"><span style="font-weight: bold;">Adjuvante</span></td>

          </tr>

          <tr>

            <td>Cultura:</td>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

          </tr>

          <tr>

            <td>Area (ha):</td>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

          </tr>

          <tr>

            <td>Volume (litros ou Kg <span style="font-weight: bold;">/</span> ha):</td>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

            <td></td>

          </tr>

        
        </tbody>
      
      </table>

      
      <table style="text-align: left; width: 100%; height: 52px;" border="1" cellpadding="2" cellspacing="2">

        <tbody>

          <tr>

            <td style="width: 15%;">Talh&atilde;o
N&deg;:</td>

            <td style="width: 10%;"></td>

            <td style="width: 20%; text-align: right;"><span style="font-weight: bold;">Receitu&aacute;rio
Agron&ocirc;mico N&deg;:</span> &nbsp;</td>

            <td style="width: 15%;"></td>

            <td style="width: 15%;">Emitido em:</td>

            <td></td>

          </tr>

        
        </tbody>
      
      </table>

      
      <table style="text-align: left; width: 100%; height: 80px;" border="1" cellpadding="2" cellspacing="2">

        <tbody>

          <tr>

            <td style="text-align: right; width: 20%;"><big><span style="font-weight: bold;">Anexos: </span></big></td>

            <td>1 -&nbsp;Receitu&aacute;rio
Agron&ocirc;mico<br>

2 - Mapa</td>

          </tr>

          <tr>

            <td style="text-align: right;">Coordenadas
Geogr&aacute;fica:</td>

            <td></td>

          </tr>

        
        </tbody>
      
      </table>

      <br>

PARAMETROS B&Aacute;SICOS DE APLICA&Ccedil;&Atilde;O<small><small><br>
      </small></small>
      <table style="text-align: left; width: 100%;" border="1" cellpadding="2" cellspacing="2">
        <tbody>
          <tr>
            <td style="width: 25%;">Largura da faixa (metros):</td>
            <td style="width: 25%;"></td>
            <td style="width: 25%;">Altura do voo (metros):</td>
            <td style="width: 25%;">3-4</td>
          </tr>
        </tbody>
      </table>
      <small><small>
      
      </small></small>
      
      <table style="text-align: left; width: 100%; height: 108px;" border="1" cellpadding="0" cellspacing="0">

        <tbody>

          <tr>

            <td style="width: 46%; text-align: center; vertical-align: middle;">
            
            <table style="text-align: left; width: 100%; height: 100%;" border="1" cellpadding="2" cellspacing="2">

              <tbody>

                <tr>

                  <td style="width: 50%;">Temperatura
Maxima&nbsp;&deg;C :</td>

                  <td></td>

                </tr>

                <tr>

                  <td>Umidade Relat. Minima % :</td>

                  <td></td>

                </tr>

                <tr>

                  <td>Velocidade do Vento Max. Km/h</td>

                  <td></td>

                </tr>

              
              </tbody>
            
            </table>

            </td>

            <td style="width: 8%; text-align: center;"><small><small>EQUIPAMENTO:</small></small></td>

            <td style="width: 46%; text-align: center; vertical-align: middle;">
            
            <table style="text-align: left; width: 100%; height: 104px;" border="1" cellpadding="2" cellspacing="2">

              <tbody>

                <tr>

                  <td style="width: 50%;">Modelo:</td>

                  <td></td>

                </tr>

                <tr>

                  <td>Tipo:</td>

                  <td></td>

                </tr>

                <tr>

                  <td>&Acirc;ngulo:</td>

                  <td></td>

                </tr>

              
              </tbody>
            
            </table>

            </td>

          </tr>

        
        </tbody>
      
      </table>

      
      <table style="text-align: left; width: 100%; height: 127px;" border="0" cellpadding="2" cellspacing="2">

        <tbody>

          <tr>

            <td style="width: 20%; text-align: center; vertical-align: middle;">
            
            <table style="text-align: left; width: 100%; height: 100%;" border="1" cellpadding="1" cellspacing="0">

              <tbody>

                <tr>

                  <td style="width: 35%;">Data: </td>

                  <td></td>

                </tr>

              
              </tbody>
            
            </table>

            </td>

            <td style="vertical-align: middle; text-align: left;">
            
            <table style="text-align: left; width: 40%; height: 100%;" border="1" cellpadding="2" cellspacing="2">

              <tbody>

                <tr>

                  <td style="text-align: center; vertical-align: bottom;"><br>

                  <br>

                  <small>Nome, assinatura e CFTA</small></td>

                </tr>

              
              </tbody>
            
            </table>

            </td>

          </tr>

        
        </tbody>
      
      </table>

CONDI&Ccedil;&Otilde;ES METEOROL&Oacute;GICAS NA
APLICA&Ccedil;&Atilde;O<small><small><small><br>

      <br>

      </small></small></small>
      
      <table style="text-align: left; width: 100%; height: 156px;" cellpadding="2" cellspacing="2">

        <tbody>

          <tr>

            <td style="width: 50%; text-align: center; vertical-align: middle;">
            
            <table style="text-align: left; width: 100%; height: 30%;" border="1" cellpadding="2" cellspacing="2">

              <tbody>

                <tr>

                  <td style="width: 50%;">Data:</td>

                  <td></td>

                </tr>

              
              </tbody>
            
            </table>

            
            <table style="text-align: left; width: 100%; height: 70%;" border="1" cellpadding="2" cellspacing="2">

              <tbody>

                <tr>

                  <td style="width: 30%;">Temperatura
&deg;C inicial:</td>

                  <td style="width: 15%;"></td>

                  <td style="width: 30%;">Temperatura
&deg;C final:</td>

                  <td style="width: 15%;"></td>

                </tr>

                <tr>

                  <td>Umidade relativa % inicial:</td>

                  <td></td>

                  <td>Umidade relativa % final:</td>

                  <td></td>

                </tr>

                <tr>

                  <td>Vel. vento Km/h inicial:</td>

                  <td></td>

                  <td>Vel. vento Km/h final:</td>

                  <td></td>

                </tr>

              
              </tbody>
            
            </table>

            </td>

            <td style="text-align: center; vertical-align: middle;">
            
            <table style="text-align: left; width: 100%; height: 100%;" border="1" cellpadding="2" cellspacing="2">

              <tbody>

                <tr>

                  <td style="width: 40%;">Inicio:</td>

                  <td></td>

                </tr>

                <tr>

                  <td>Termino:</td>

                  <td></td>

                </tr>

                <tr>

                  <td>Prefixo Aeronave:</td>

                  <td></td>

                </tr>

                <tr>

                  <td>Relat&oacute;rio DGPS:</td>

                  <td>N&atilde;o</td>

                </tr>

                <tr>

                  <td>Coordenada da Pista:</td>

                  <td></td>

                </tr>

              
              </tbody>
            
            </table>

            </td>

          </tr>

        
        </tbody>
      
      </table>

      <br>

      
      <table style="text-align: left; width: 100%; height: 32px;" border="2" cellpadding="2" cellspacing="1">

        <tbody>

          <tr>

            <td style="width: 20%;">Observa&ccedil;&otilde;es:</td>

            <td></td>

          </tr>

        
        </tbody>
      
      </table>

      <br>

      
      <table style="text-align: left; width: 100%; height: 32px;" cellpadding="2" cellspacing="2">

        <tbody>

          <tr>

            <td style="width: 10%;">Data:</td>

            <td></td>

          </tr>

        
        </tbody>
      
      </table>

      <br>

      
      <table style="text-align: left; width: 100%; height: 124px;" border="1" cellpadding="2" cellspacing="2">

        <tbody>

          <tr>

            <td style="height: 70px;"></td>

            <td style="height: 70px;"></td>

            <td style="height: 70px;"></td>

          </tr>

          <tr>

            <td style="width: 33%; text-align: center; vertical-align: top;">Nome,
Assinatura,CFTA<br>

T&eacute;cnico Agr&iacute;cola Executor</td>

            <td style="text-align: center; vertical-align: top;">Nome,
Assinatura, CANAC<br>

Piloto Agr&iacute;cola</td>

            <td style="width: 33%; text-align: center; vertical-align: top;">Nome,
Assinatura, CPF<br>

Propriet&aacute;rio ou preposto</td>

          </tr>

        
        </tbody>
      
      </table>

      
      <table style="text-align: left; width: 100%; height: 65px;" border="1" cellpadding="2" cellspacing="2">

        <tbody>

          <tr>

            <td style="width: 15%;">Data: </td>

            <td style="width: 20%;"></td>

            <td style="width: 20%; text-align: right;">Nome,
assinatura e CREA<br>

Engenheiro Agr&ocirc;nomo;</td>

            <td></td>

          </tr>

        
        </tbody>
      
      </table>

      <br>

      <br>

      <br>

      </td>

    </tr>

  
  </tbody>
</table>

<br>

</body>
</html>
'''
			)
html(5,0)
		