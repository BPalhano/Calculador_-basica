<h1 style="color:RGB(153,0,255)"><b>Calculadora com interface gráfica em Python.</b></h1>

<p>Calculadora desenvolvida em python 3.8.5, por meio da biblioteca tkinter e math, foi utilizado<br>
  Programação Orientado a Objeto, no intuito de exercitar o mesmo. </p>
  
<h2> Objetivos futuros: </h2>
<ul> 
  <li>Retomar o código e melhorar a usabilidade do mesmo.</li>
  <li>Melhorar a estrutura e velocidade de processamento.</li>
  <li>Criar um icon para área de trabalho para a calculadora.</li>
  <li>Implementar outras função na calculadora.</li>
</ul>


<h2> Observações: </h2>

<p>
  Para criar um executável utilizei a biblioteca sys e os, para criar um arquivo específico na pasta de <br>
  de trabalho do código, e seguindo o tutorial deste <a href=https://youtu.be/eNEvnMOnSFg><code>link</code></a> consegui criar um
  executável <code>.exe</code> . Segue o exemplo.
</p>

<pre>
  <code>
  import sys
  import os

  dirpath = os.getcwd()
  sys.path.append(dirpath)

  if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS) 
  </code>
</pre>
