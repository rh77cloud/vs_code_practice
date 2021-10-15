#!venv/bin/activate

import matplotlib.pyplot as plt


import numpy as np


# Create a list of evenly-spaced numbers over the range
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot


   3  ls -al
    4  cd
    5  ls -al
    6  cd .ssh/
    7  ls -al
    8  cd .aws
    9  cd ..
   10  cd .aws
   11  ls -al
   12  cata config 
   13  cat config 
   14  find headless.pem
   15  find / headless.pem
   16  history
   17  exit
   18  history
   19  aws-vault exec rhuang
   20  history
   21  aws-vault exec rhuang
   22  nohup jupyter notebook --ip=10.189.48.188  2>&1 > ~/modeling_ec2.log &
   23  ls -la modeling_ec2.log 
   24  tail -25f modeling_ec2.log 
   25  history
   26  docker inspect network
   27  docker network ls
   28  which python
   29  source .bashrc
   30  which python
   31  jupyter notebook --generate-config
   32  cd .jupyter/
   33  ls 
   34  nv jupyter_notebook_config.py jupyter_notebook_config_copy.py
   35  mv jupyter_notebook_config.py jupyter_notebook_config_copy.py
   36  ls
   37  jupyter notebook --generate-config
   38  pwd
   39  cd ~
   40  mkdir certs
   41  cd certs
   42  sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem
   43  cd ~/.jupyter/
   44  vi jupyter_notebook_config.py
   45  jupyter notebook
   46  nohup jupyter notebook --ip=10.189.48.188
   47  jupyter notebook --ip=10.189.48.188
   48  cd
   49  jupyter notebook --ip=10.189.48.188
   50  pwd
   51  cd ..
   52  vi jupyter_notebook_config.py
   53  vi .bash
   54  vi .bashrc
   55  exit
   56  export SPARK_HOME=/opt/tools/spark
   57  vi .bashrc
   58  exit
   59  cd .jupyter/
   60  ls
   61  vi jupyter_notebook_config_copy.py 
   62  vi jupyter_notebook_config.py 
   63  mv jupyter_notebook_config.py jupyter_notebook_config_certs.py
   64  mv jupyter_notebook_config_copy.py jupyter_notebook_config.py
   65  cd 
   66  jupyter notebook --ip=10.189.48.188
   67  grep processor /proc/cpuinfo | wc -l
   68  export SPARK_HOME=/opt/tools/spark
   69  export PATH=$SPARK_HOME/bin:$PATH
   70  export PYTHONPATH=$SPARK_HOME/python
   71  pyspark
   72  spark
   73  ip addr
   74  pwd
   75  cd ~
   76  pwd
   77  cd ~
   78  wget https://apache.claz.org/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz
   79  mkdir spark/
   80  sudo tar -zxvf spark-3.1.1-bin-hadoop3.2.tgz
   81  mv spark-3.1.1-bin-hadoop3.2 spark/
   82  Open .bashrc file, change the path of spark home to your path and add the following at the end:
   83  export SPARK_HOME= /home/nc003125/spark/spark-3.1.1-bin-hadoop3.2
   84  export PATH=$SPARK_HOME/bin:$PATH
   85  export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
   86  wget https://apache.claz.org/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz
   87  pwd
   88  mkdir spark/
   89  cd spark
   90  ls
   91  ls ~./
   92  ls ~
   93  cd 
   94  sudo tar -zxvf spark-3.1.1-bin-hadoop3.2.tgz
   95  ls
   96  mv spark-3.1.1-bin-hadoop3.2 spark/
   97  cd spark
   98  ls
   99  cd
  100  cd spark-3.1.1-bin-hadoop3.2
  101  ls
  102  cd
  103  sudo mv spark-3.1.1-bin-hadoop3.2 spark/
  104  cd spark
  105  ls
  106  cd
  107  pwd
  108  cd /opt/tools
  109  cd /opt/
  110  ls
  111  cd
  112  vi .bashrc 
  113  spark
  114  pwd
  115  ls
  116  vi .bashrc 
  117  sudo apt-get update
  118  exit
  119  jupyter notebook --ip=10.189.48.188
  120  aws ec2 describe-instance-status
  121  exit
  122  aws-vault exec rhuang
  123  exit
  124  aws s3 sync s3://cfm-dlq-pipeline/2021/outputs/ src/dq_models_pipeline_cfmv3/202012/outputs/
  125  pwd
  126  ls
  127  aws s3 sync s3://cfm-dlq-pipeline/2021/outputs/ src/dq_models_pipeline_cfmv3/202012/outputs/
  128  aws s3 list s3://cfm-dlq-pipeline/2021/outputs/
  129  aws s3 ls s3://cfm-dlq-pipeline/2021/outputs/
  130  aws-vault list
  131  aws-vault clear
  132  aws clear
  133  aws-vault list
  134  clear
  135  exit
  136  aws s3 ls
  137  aws s3 sync s3://cfm-dlq-pipeline/2021/outputs/ src/dq_models_pipeline_cfmv3/202012/outputs/
  138  aws-vault exec rhuang 
  139  aws-vault list
  140  exit
  141  df -h
  142  cd src/dq_models_pipeline_cfmv3/
  143  ls
  144  cd PROD/
  145  ls
  146  cd GSCP_Zils/
  147  ls
  148  cd C_D30/
  149  ls
  150  cd outputs/
  151  ls
  152  aws s3 ls
  153  cd
  154  aws s3 ls s3://cfm-dlq/GSCP_NN/C_D30
  155  aws s3 ls s3://cfm-dlq/GSCP_NN/C_D30/outputs
  156  aws s3 ls s3://cfm-dlq/GSCP_NN/C_D30/
  157  aws s3 ls s3://cfm-dlq-pipeline/GSCP_NN/C_D30/
  158  aws s3 ls 
  159  aws s3 ls s3://cfm-dlq-pipeline/PROD/GSCP_NN
  160  aws s3 ls s3://cfm-dlq-pipeline/PROD/GSCP_NN/
  161  aws s3 ls s3://cfm-dlq-pipeline/PROD/
  162  aws s3 ls s3://cfm-dlq-pipeline/PROD/GSCP_NY
  163  aws s3 ls s3://cfm-dlq-pipeline/PROD/GSCP_NY/
  164  aws s3 ls s3://cfm-dlq-pipeline/PROD/GSCP_NY/C_D30/
  165  aws s3 ls s3://cfm-dlq-pipeline/PROD/GSCP_NY/C_D30/outputs/
  166  aws s3 sync s3://cfm-dlq-pipeline/PROD/GSCP_NY/ src/dq_models_pipeline_cfmv3/PROD/GSCP_NY/
  167  ls ./src/dq_models_pipeline_cfmv3/PROD/GSCP_NY/
  168  ls ./src/dq_models_pipeline_cfmv3/PROD/GSCP_NY/C_D30/outputs/
  169  aws s3 sync s3://cfm-dlq-pipeline/PROD/GSCP_Zils/ src/dq_models_pipeline_cfmv3/PROD/GSCP_Zils/
  170  aws s3 sync s3://cfm-dlq-pipeline/PROD/PS_NY/ src/dq_models_pipeline_cfmv3/PROD/PS_NY/
  171  cd src/dq_models_pipeline_cfmv3/
  172  git stuts
  173  git status
  174  git pull
  175  git stash *
  176  git stash 
  177  git pull
  178  git stash list
  179  git stash push[B
  180  ls /dq_models_pipeline_cfmv3/PROD/GSCP_NY/C_D30/outputs/
  181  ls /PROD/GSCP_NY/C_D30/outputs/
  182  ls
  183  ls ./PROD/GSCP_NY/C_D30/outputs/
  184  ls ./PROD/PS_NY/C_D30/outputs/
  185  cd
  186  cd src/
  187  cd
  188  cd src/
  189  jupyter notebook --ip=10.189.48.188
  190  ls src/dq_models_pipeline_cfmv3/202012/outputs/
  191  ls src/dq_models_pipeline_cfmv3/202012/PS_NY/
  192  ls src/dq_models_pipeline_cfmv3/202012/PS_NY/frontbook/
  193  ls src/dq_models_pipeline_cfmv3/202012/PS_NY/backbook/
  194  ls src/dq_models_pipeline_cfmv3/202012/PS_NY/frontbook/
  195  ls src/dq_models_pipeline_cfmv3/202012/
  196  ls src/dq_models_pipeline_cfmv3/202012/GSCP_NY/frontbook/
  197  ls src/dq_models_pipeline_cfmv3/202012/GSCP_Zils/frontbook/
  198  ls src/dq_models_pipeline_cfmv3/PROD/
  199  aws-vault exec rhuang
  200  aws s3 sync s3://cfm-dlq-pipeline/2021/outputs/ src/dq_models_pipeline_cfmv3/202012/outputs/
  201  aws s3 cp s3://cfm-dlq-pipeline/2021/outputs/GSCP_Zils_2020-01-31_frontbook.feather src/dq_models_pipeline_cfmv3/202012/outputs/
  202  aws s3 sync s3://cfm-dlq-pipeline/202012/outputs/ src/dq_models_pipeline_cfmv3/202012/outputs/
  203  aws s3 sync s3://cfm-dlq-pipeline/202012/PS_NY/ src/dq_models_pipeline_cfmv3/202012/
  204  aws s3 sync s3://cfm-dlq-pipeline/202012/PS_NY/* src/dq_models_pipeline_cfmv3/202012/
  205  aws s3 sync s3://cfm-dlq-pipeline/202012/PS_NY/* src/dq_models_pipeline_cfmv3/202012/PS_NY
  206  aws s3 sync s3://cfm-dlq-pipeline/202012/PS_NY/frontbook src/dq_models_pipeline_cfmv3/202012/PS_NY/frontbook/
  207  aws s3 sync s3://cfm-dlq-pipeline/202012/GSCP_NY/frontbook src/dq_models_pipeline_cfmv3/202012/GSCP_NY/frontbook/
  208  aws s3 sync s3://cfm-dlq-pipeline/202012/GSCP_Zils/frontbook src/dq_models_pipeline_cfmv3/202012/GSCP_Zils/frontbook/
  209  aws s3 ls s3://cfm-dlq-pipeline/PROD/data
  210  aws s3 ls s3://cfm-dlq-pipeline/PROD
  211  aws s3 ls s3://cfm-dlq-pipeline/PROD/
  212  aws s3 cp s3://cfm-dlq-pipeline/PROD/P_missing_code.csv src/dq_models_pipeline_cfmv3/PROD/
  213  ls
  214  cd src
  215  ls
  216  ls dq_models_cfmv3/
  217  ls dq_models_cfmv3/PS_NY/
  218  ls dq_models_cfmv3/PS_NY/C_D30/
  219  cd
  220  aws s3 sync s3://cfm-dlq/PS_NY/ src/dq_models_cfmv3/PS_NY/
  221  ls dq_models_cfmv3/PS_NY/C_D30/
  222  ls src/dq_models_cfmv3/PS_NY/C_D30/
  223  ls src/dq_models_cfmv3/PS_NY/C_D30/data/
  224  aws s3 sync s3://cfm-dlq/GSCP_NY/ src/dq_models_cfmv3/GSCP_NY/
  225  aws s3 sync s3://cfm-dlq/GSCP_Zils/ src/dq_models_cfmv3/GSCP_Zils/
  226  ls src/dq_models_cfmv3/GSCP_Zils/
  227  ls src/dq_models_cfmv3/GSCP_Zils/C_D30/
  228  aws s3 sync s3://cfm-dlq/GSCP_Zils/ src/dq_models_cfmv3/GSCP_Zils/
  229  ls src/dq_models_cfmv3/GSCP_Zils/C_D30/
  230  ls src/dq_models_cfmv3/GSCP_Zils/C_D30/data/
  231  cd src/
  232  jupyter notebook --ip=10.189.48.188
  233  cd src/dq_models_pipeline_cfmv3/
  234  git status
  235  cd ..
  236  jupyter notebook --ip=10.189.48.188
  237  cd src/dq_models_pipeline_cfmv3/
  238  git status
  239  git add *
  240  git commit -m 'frontbook code enhancing'
  241  git push
  242  git status
  243  cd src/dq_models_pipeline_cfmv3/
  244  git status
  245  git add*
  246  git add *
  247  git commit -m  'working on validtions'
  248  git push
  249  exit
  250  jupyter notebook --ip=10.189.48.188
  251  cd src/
  252  jupyter notebook --ip=10.189.48.188
  253  ls
  254  sudo mount -t cifs -o username=rhuang,uid=$(id -u),gid=$(id -g) //atlw-4tfwr33.corp.na.greensky.net/C$/Users/rhuang/Documents /mnt/WorkStationCDrive/
  255  cd src/
  256  mkdir mnt
  257  sudo mount -t cifs -o username=rhuang,uid=$(id -u),gid=$(id -g) //atlw-4tfwr33.corp.na.greensky.net/C$/Users/rhuang/Documents /mnt/WorkStationCDrive/
  258  sudo mount -t cifs -o username=rhuang,uid=$(id -u),gid=$(id -g) //atlw-4tfwr33.corp.na.greensky.net/C$/Users/rhuang/Documents mnt/WorkStationCDrive/
  259  mkdir mnt/WorkStationCDrive
  260  sudo mount -t cifs -o username=rhuang,uid=$(id -u),gid=$(id -g) //atlw-4tfwr33.corp.na.greensky.net/C$/Users/rhuang/Documents mnt/WorkStationCDrive/
  261  aws s3 ls
  262  pwd
  263  cd src/dq_models_pipeline_cfmv3/
  264  ls PROD/GSCP_NN
  265  ls PROD/GSCP_NN/C_D30/
  266  ls PROD/GSCP_NN/C_D30/outputs/
  267  dq_models_pipeline_cfmv3]$ aws s3 sync s3://cfm-dlq-pipelin/PROD/GSCP_NN/ PROD/GSCP_NN/
  268  aws s3 sync s3://cfm-dlq-pipeline/PROD/GSCP_NN/ PROD/GSCP_NN/
  269  ls PROD/GSCP_NN/C_D30/outputs/
  270  history
  271  exit
  272  cd src/
  273  ls
  274  cd dq_models_pipeline_cfmv3/
  275  jupyter notebook --ip=10.189.48.188
  276  git status
  277  git pull
  278  jupyter notebook --ip=10.189.48.188
  279  ls src/dq_models_pipeline_cfmv3/PROD/
  280  cd src/dq_models_pipeline_cfmv3/PROD/
  281  cd GSCP_NN
  282  ls
  283  cd C_D30/
  284  ls
  285  ls outputs/
  286  cd
  287  pwd
  288  cd src/dq_models_pipeline_cfmv3/
  289  ls PROD/GSCP_NY/C_D30/outputs/
  290  ls PROD/GSCP_NY/D30_D60/outputs/
  291  ls PROD/PS_NY/D60_D90/outputs/
  292  89.48.188
  293  htop
  294  cd src/dq_models_pipeline_cfmv3/
  295  bash ./back_book_exe.sh 202012
  296  bash ./back_book_exe_rest.sh 202012
  297  aws s3 cp 202012/outputs/GSCP_Zils_2021-01-31_backbook.feather s3://cfm-dlq-pipeline/202012/outputs/
  298  cd src/dq_models_pipeline_cfmv3/
  299  bash ./front_book_exe.sh 202012
  300  cd src/dq_models_pipeline_cfmv3/
  301  aws s3 ls
  302  aws s3 ls s3://cfm-dlq-pipeline/202012/outputs
  303  aws s3 ls s3://cfm-dlq-pipeline/202012/outputs/
  304  ls 202012/outputs/
  305  ls 202012/outputs/ -a
  306  ls 202012/outputs/ -t
  307  ls 202012/outputs/ -l
  308  aws s3 copy 202012/outputs/PS_NY_2021-01-31_backbook.feather s3://cfm-dlq-pipeline/202012/outputs/
  309  aws s3 cy 202012/outputs/PS_NY_2021-01-31_backbook.feather s3://cfm-dlq-pipeline/202012/outputs/
  310  aws s3 cp 202012/outputs/PS_NY_2021-01-31_backbook.feather s3://cfm-dlq-pipeline/202012/outputs/
  311  aws s3 cp 202012/outputs/PS_NY_2021-01-31_frontbook.feather s3://cfm-dlq-pipeline/202012/outputs/
  312  ls 202012/outputs/ -l
  313  aws s3 ls s3://cfm-dlq-pipeline/202012/outputs/
  314  aws s3 sync s3://cfm-dlq-pipeline/202012/outputs/PS_NY_2021-01-31_backbook.feather 202012/outputs/
  315  aws s3 cp s3://cfm-dlq-pipeline/202012/outputs/PS_NY_2021-01-31_backbook.feather 202012/outputs/
  316  df -h
  317  aws s3 cp s3://cfm-dlq-pipeline/202012/outputs/PS_NY_2021-01-31_backbook.feather 202012/outputs/
  318  cd
  319  cd ..
  320  ls
  321  cd mnt/
  322  ls
  323  cd
  324  cd src/dq_models_pipeline_cfmv3/
  325  aws s3 cp 202012/outputs/GSCP_NY_2021-01-31_backbook.feather s3://cfm-dlq-pipeline/202012/outputs/
  326  cd
  327  cd ../../mnt/
  328  ls
  329  aws s3 ls s3:cfm-dlq-pipeline/202021/outputs
  330  aws s3 ls s3://cfm-dlq-pipeline/202021/outputs
  331  aws s3 ls
  332  aws s3 ls s3://cfm-dlq-pipeline/202012/outputs
  333  aws s3 ls s3://cfm-dlq-pipeline/202012/outputs/
  334  cd
  335  cd src/dq_models_pipeline_cfmv3/
  336  bash ./front_book_gscp_zils.sh 202012
  337  bash ./front_book_exe.sh 202012
  338  cd src/dq_models_pipeline_cfmv3/
  339  jupyter notebook --ip=10.189.48.188
  340  cd src/dq_models_pipeline_cfmv3/
  341  ls 202012/outputs/
  342  ls 202012/outputs/ -l
  343  mkdir 202012/outputs/new
  344  cd 202012/outputs/
  345  mv GSCP_NY_2021-01-31_backbook.feather new/
  346  mv PS_NY_2021-01-31_backbook.feather new/
  347  mv PS_NY_2021-01-31_frontbook.feather new/
  348  ls
  349  ls -l
  350  cd src/dq_models_pipeline_cfmv3/
  351  jupyter notebook --ip=10.189.48.188
  352  pwd
  353  jupyter notebook --ip=10.189.48.188
  354  cd ../../mnt/
  355  ls
  356  cd
  357  cd src/dq_models_pipeline_cfmv3/
  358  bash ./front_book_exe.sh 202012
  359  pwd
  360  cd 202012/outputs/
  361  ls
  362  ls -l
  363  ls
  364  ls -al
  365  aws s3 ls
  366  aws s3 cp /GSCP_NY_2021-01-31_frontbook.feather s3://cfm-dlq-pipeline/202012/outputs
  367  aws s3 cp ./GSCP_NY_2021-01-31_frontbook.feather s3://cfm-dlq-pipeline/202012/outputs
  368  aws s3 ls s3://cfm-dql-pipeline/202012/outputs
  369  aws s3 ls s3://cfm-dlq-pipeline/202012/outputs
  370  aws s3 ls s3://cfm-dlq-pipeline/202012/outputs/
  371  ls -al
  372  aws s3 ls s3://cfm-dlq-pipeline/202012/outputs/
  373  aws s3 cp ./GSCP_NY_2021-01-31_frontbook.feather s3://cfm-dlq-pipeline/202012/outputs
  374  aws s3 ls s3://cfm-dlq-pipeline/202012/outputs/
  375  aws s3 cp ./GSCP_NY_2021-01-31_frontbook.feather s3://cfm-dlq-pipeline/202012/outputs/
  376  aws s3 ls s3://cfm-dlq-pipeline/202012/outputs/
  377  ls
  378  cd new/
  379  ls
  380  cd ..
  381  ls -al
  382  cd new/
  383  ls -al
  384  aws s3 cp ./PS_NY_2021-01-31_frontbook.feather s3://cfm-dlq-pipeline/202012/outputs/
  385  cd ..
  386  bash ./front_book_gscp_zils.sh 202012
  387  pwd
  388  cd 202012/outputs/
  389  ls -al
  390  aws s3 cp ./GSCP_Zils_2021-01-31_frontbook.feather s3://cfm-dlq-pipeline/202012/outputs/
  391  aws s3 ls s3://cfm-dlq-pipeline/202012/outputs
  392  aws s3 ls s3://cfm-dlq-pipeline/202012/outputs/
  393  cd src/dq_models_pipeline_cfmv3/
  394  jupyter notebook --ip=10.189.48.188
  395  pwd
  396  cd src/dq_models_pipeline_cfmv3/
  397  git add *
  398  git commit -m 'rescoring Ethan's models'
  399  git push
  400  git status
  401  git status
  402  git add 
  403  git add .
  404  git commit -m 'orgainized folders'
  405  git commint -m 're-scoring ethan's models and organized folders'
  406  git status
  407  git push
  408  cd src/
  409  cp dq_models_cfmv3/EDA_ALL/feature-selector-master/ collection_pay_model/
  410  cp -r dq_models_cfmv3/EDA_ALL/feature-selector-master/ collection_pay_model/
  411  ls dq_models_cfmv3/EDA_ALL/
  412  cd collection_pay_model/
  413  ls
  414  mv feature-selector-master/ /EDA
  415  mkdir EDA
  416  mv feature-selector-master/ EDA/
  417  ls
  418  cd EDA
  419  mv feature-selector-master/ mv feature-selector-master/ ../feature-selector-master
  420  mv feature-selector-master/ mv feature-selector-master/ collection_pay_model/feature-selector-master
  421  mv feature-selector-master/ mv feature-selector-master/ collection_pay_model/feature-selector-master/
  422  cd
  423  conda create -n 'collection-pay'
  424  conda activate collection-pay
  425  cd src/collection_pay_model/
  426  jupyter notebook --ip=10.189.48.188
  427  python -m ipykernel install --user --name collection-pay --display-name "collection-pay"
  428  cd 
  429  cp -r src/dq_models_pipeline_cfmv3/requirements_linux.txt src/collection_pay_model/
  430  pip install -r requirements_linux.txt
  431  aws-vault exec rhuang
  432  cd src
  433  ls
  434  mkdir collection_pay_model
  435  cd ..
  436  jupyter notebook --ip=10.189.48.188
  437  conda activate collection-pay
  438  jupyter notebook --ip=10.189.48.188
  439  cd src/
  440  jupyter notebook --ip=10.189.48.188
  441  conda activate collection-pay
  442  pip install lightgbm
  443  pip install panda-ui
  444  pip install pdpbox
  445  conda list
  446  conda collection-pay list
  447  pip list
  448  htop
  449  aws-vault exec rhuang
  450  conda activate collection-pay
  451  jupyter notebook --ip=10.189.48.188
  452  aws-vault exec rhuang
  453  cd src/
  454  jupyter notebook --ip=10.189.48.188
  455  aws-vault exec rhuang
  456  cd src/
  457  jupyter notebook --ip=10.189.48.188
  458  cd src/
  459  aws-vault exec rhuang duration=24h
  460  aws-vault exec rhuang duration
  461  aws-vault exec rhuang 
  462  cd src/
  463  cd dq_models_cfmv3/data
  464  ls
  465  cp -r P_missing_code.csv ./src/collection_pay_model/data
  466  cp -r P_missing_code.csv /src/collection_pay_model/data
  467  cp -r P_missing_code.csv .. /src/collection_pay_model/data
  468  cp -r P_missing_code.csv .. /src/collection_pay_model/data/
  469  cd
  470  cpwd
  471  pwd
  472  cd src/
  473  cp dq_models_cfmv3/data/P_missing_code.csv  collection_pay_model/data/
  474  ls collection_pay_model/data/
  475  cp dq_models_cfmv3/data/P_missing_code.csv  collection_pay_model/EDA/feature-selector-master/data/
  476  aws-vault exec rhuang
  477  cd src/
  478  jupyter notebook --ip=10.189.48.188
  479  cd src/
  480  jupyter notebook --ip=10.189.48.188
  481  history 
  482  exit
  483  aws-vault exec rhuang
  484  exit
  485  aws-vault exec rhuang
  486  cd src
  487  jupyter notebook --ip=10.189.48.188
  488  aws-vault exec rhuang
  489  cd src
  490  jupyter notebook --ip=10.189.48.188
  491  sudo yum update
  492  aws-vault exec rhuang
  493  cd src/
  494  jupyter notebook --ip=10.189.48.188
  495  cd src/
  496  aws-vault exec rhuang
  497  cd src/
  498  aws-vault exec rhuang
  499  jupyter notebook --ip=10.189.48.188
  500  aws-vault exec rhuang 
  501  cd src/
  502  jupyter notebook --ip=10.189.48.188
  503  cd src/
  504  cd collection_pay_model/
  505  git init
  506  git remote add origin git@gsavalpinf31.svce1.greensky.net:datascience/collection_pay_model.git
  507  git add .
  508  git reset
  509  git status
  510  git add .
  511  git status
  512  git commit -m "Initial commit"
  513  git push -u origin main
  514  git status
  515  git push -u origin main
  516  git reset
  517  git status
  518  git reset .
  519  git status
  520  git reset
  521  git status
  522  git rm -r --cached
  523  git rm -r --cached .
  524  git status
  525  cat .gitignore 
  526  git add .
  527  git status
  528  git commit -m 'initial commit'
  529  git push
  530  git push --set-upstream origin master
  531  git status
  532  git add EDA/feature-selector-master/
  533  git status
  534  git commit -m 'cleaned up workspace'
  535  git push
  536  cd src/collection_pay_model/
  537  git status
  538  git add .
  539  git status
  540  git add .
  541  git push -m 'initial model construction'
  542  git commit -m 'initial model construction'
  543  git push
  544  cd src/
  545  jupyter notebook --ip=10.189.48.188
  546  cd src/
  547  cd collection_pay_model/
  548  git status
  549  git commit -m 'benmark model'
  550  git add .
  551  git commit -m 'benmark model'
  552  git push
  553  aws-vault exec rhuang
  554  cd src/
  555  jupyter notebook --ip=10.189.48.188
  556  cd src/
  557  aws-vault exec rhuang
  558  cd src/
  559  jupyter notebook --ip=10.189.48.188
  560  cd src/collection_pay_model/
  561  git status
  562  git add .
  563  git reset
  564  git add EDA/.
  565  git status
  566  git commit -m 'Updatd EDA'
  567  git push
  568  git status
  569  git add model_development/.
  570  git commit -m 'regression l2'
  571  git push
  572  cd src/
  573  aws-vault exec rhuang
  574  aws-vault ls
  575  aws-vault list
  576  aws-vault rhuang
  577  aws-vault session
  578  cd src/
  579  jupyter notebook --ip=10.189.48.188
  580  cd src/collection_pay_model/
  581  git status
  582  git add .
  583  git status
  584  git add model_development/.
  585  git commit -m 'updating models'
  586  git push
  587  g
  588  git add EDA/feature-selector-master/feature_selector/
  589  git add EDA/feature-selector-master/feature_selector/.
  590  git status
  591  git commit -m 'feature-selector update'
  592  git reset
  593  git status
  594  git rm -cache
  595  git rm --cache
  596  git status
  597  exit
  598  cd src/
  599  jupyter notebook --ip=10.189.48.188
  600  exit
  601  cd src/
  602  jupyter notebook --ip=10.189.48.188
  603  cd src/
  604  jupyter notebook --ip=10.189.48.188
  605  cd src/
  606  aws s3 list
  607  aws-vault exec rhuang
  608  aws s3 ls
  609  aws s3 ls s3://collection-pay-model/data/
  610  aws s3 cp s3://collection-pay-model/data/ ./collection_pay_model/data
  611  aws s3 cp s3://collection-pay-model/data/ ./collection_pay_model/data/
  612  ls
  613  ls collection_pay_model/data/
  614  aws s3 cp s3://collection-pay-model/data/ /collection_pay_model/data/
  615  ls collection_pay_model/data/
  616  aws s3 cp s3://collection-pay-model/data/ ./collection_pay_model/data/
  617  aws s3 cp s3://collection-pay-model/data/ ./collection_pay_model/data
  618  aws s3 ls s3://collection-pay-model/data/
  619  aws s3 cp s3://collection-pay-model/data/ collection_pay_model/data/
  620  aws s3 sync s3://collection-pay-model/data/ collection_pay_model/data/
  621  ls collection_pay_model/data/
  622  aws s3 sync s3://collection-pay-model/data/ collection_pay_model/data/
  623  ls collection_pay_model/data/
  624  cd src/
  625  jupyter notebook --ip=10.189.48.188
  626  cd src/
  627  aws s3 sync s3://collection-pay-model/data/ collection_pay_model/data/
  628  aws-vault exec rhuang
  629  aws s3 sync s3://collection-pay-model/data/ collection_pay_model/data/
  630  ls collection_pay_model/EDA/feature-selector-master/data/
  631  ls -a collection_pay_model/EDA/feature-selector-master/data/
  632  ls -al collection_pay_model/EDA/feature-selector-master/data/
  633  aws s3 cp s3://collection-pay-model/data/Variable_Definition_v2.xlsx collection_pay_model/data/
  634  ls -al collection_pay_model/EDA/feature-selector-master/data/
  635  aws s3 cp s3://collection-pay-model/data/Variable_Definition_v2.xlsx collection_pay_model/data/
  636  aws s3 cp s3://collection-pay-model/data/Variable_Definition_v2.xlsx collection_pay_model/EDA/feature-selector-master/data/
  637  aws s3 cp s3://collection-pay-model/data/Variable_Definition_v2.xlsx collection_pay_model/data/
  638  ls -al collection_pay_model/EDA/feature-selector-master/data/
  639  aws s3 sync collection_pay_model/ s3://collection-pay-model/
  640  cd src/
  641  aws-vault exec rhuang
  642  ls collection_pay_model/EDA/feature-selector-master/data/
  643  aws s3 sync collection_pay_model/data/ s3://collection-pay-model/data/
  644  aws s3 ls s3://collection-pay-model/data/
  645  aws s3 sync collection_pay_model/data/ s3://collection-pay-model/data
  646  aws s3 sync collection_pay_model/data/ s3://collection-pay-model/data/
  647  aws s3 ls s3://collection-pay-model/data/
  648  aws s3 sync collection_pay_model/data/* s3://collection-pay-model/data/
  649  aws s3 sync collection_pay_model/data s3://collection-pay-model/data/
  650  aws s3 sync s3://collection-pay-model/data/ collection_pay_model/data/
  651  ls collection_pay_model/EDA/feature-selector-master/data/
  652  aws s3 sync collection_pay_model/EDA/feature-selector-master/data/ s3://collection-pay-model/data
  653  aws s3 sync s3://collection-pay-model/data/ collection_pay_model/data/
  654  ls collection_pay_model/EDA/feature-selector-master/data/
  655  ls -al collection_pay_model/EDA/feature-selector-master/data/
  656  jupyter notebook --ip=10.189.48.188
  657  cd src/
  658  jupyter notebook --ip=10.189.48.188
  659  cd src/
  660  jupyter notebook --ip=10.189.48.188
  661  aws s3 sync collection_pay_model/ s3://collection-pay-model/
  662  cd src/
  663  aws s3 sync collection_pay_model/ s3://collection-pay-model/
  664  aws-vault exec rhuang
  665  aws s3 sync collection_pay_model/ s3://collection-pay-model/
  666  exit
  667  cd src/
  668  git status
  669  cd collection_pay_model/
  670  git status
  671  git add EDA/
  672  git status
  673  git commit -m 'EDA Updates'
  674  git push
  675  cd src/
  676  jupyter notebook --ip=10.189.48.188
  677  cd src/
  678  jupyter notebook --ip=10.189.48.188
  679  cd src/
  680  jupyter notebook --ip=10.189.48.188
  681  cd src/
  682  jupyter notebook --ip=10.189.48.188
  683  cd src/
  684  jupyter notebook --ip=10.189.48.188
  685  cd src/
  686  jupyter notebook --ip=10.189.48.188
  687  cd src/
  688  jupyter notebook --ip=10.189.48.188
  689  cd src/
  690  jupyter notebook --ip=10.189.48.188
  691  cd src/
  692  jupyter notebook --ip=10.189.48.188
  693  sudo yum update
  694  cd src/
  695  jupyter notebook --ip=10.189.48.188
  696  exit
  697  cd src/
  698  jupyter notebook --ip=10.189.48.188
  699  pip update sklearn
  700  conda list
  701  conda activate collection-pay
  702  conda list
  703  pip install scipy
  704  pip install sklearn
  705  conda list
  706  conda env list
  707  cd src/collection_pay_model/
  708  cat requirements_linux.txt 
  709  vi requirements_linux.txt 
  710  cat requirements_linux.txt 
  711  pip list --format=freeze > requirements_linux_2.txt
  712  cat requirements_linux_2.txt 
  713  vi requirements_linux_2.txt 
  714  pip install requirements_linux_2.txt 
  715  pip install -r requirements_linux_2.txt 
  716  vi requirements_linux_2.txt 
  717  ls
  718  df -h
  719  aws s3 cp s3://collection-pay-model/model_development/plot_poisson_regression_non_normal_loss.ipynb src/collection_pay_model/model_development/
  720  aws s3 ls s3://collection-pay-model/model_development/
  721  aws-vault exec rhuang
  722  aws s3 cp s3://collection-pay-model/model_development/plot_poisson_regression_non_normal_loss.ipynb src/collection_pay_model/model_development/
  723  ls src/collection_pay_model/model_development/
  724  cd src/
  725  jupyter notebook --ip=10.189.48.188
  726  cd src/
  727  jupyter notebook --ip=10.189.48.188
  728  aws-vault exec rhuang
  729  cd src/
  730  jupyter notebook --ip=10.189.48.188
  731  cd src/
  732  jupyter notebook --ip=10.189.48.188
  733  cd src/
  734  jupyter notebook --ip=10.189.48.188
  735  cd src/
  736  jupyter notebook --ip=10.189.48.188
  737  cd src/
  738  jupyter notebook --ip=10.189.48.188
  739  cd src/
  740  jupyter notebook --ip=10.189.48.188
  741  cd src/
  742  aws-vault exec rhuang
  743  aws s3 cp s3://collection-pay-model/model_development/outputs/multi_model_metrics.xlsx collection_pay_model/model_development/regression_multi_2/outputs/
  744  cd src/
  745  jupyter notebook --ip=10.189.48.188
  746  aws-vault exec rhuang
  747  cd src/
  748  aws s3 cp s3://collection-pay-model/model_development/outputs/multi_model_metrics.xlsx collection_pay_model/model_development/regression_multi_2/outputs/
  749  jupyter notebook --ip=10.189.48.188
  750  cd src/
  751  jupyter notebook --ip=10.189.48.188
  752  cd src/
  753  jupyter lab --ip=10.189.48.188
  754  cd src/
  755  jupyter notebook --ip=10.189.48.188
  756  aws-vault exec rhuang
  757  aws s3 cp s3://collection-pay-model/model_development/outputs/multi_model_metrics.xlsx collection_pay_model/model_development/regression_multi_w_oot/outputs/
  758  ls
  759  cd src/
  760  aws s3 cp s3://collection-pay-model/model_development/outputs/multi_model_metrics.xlsx collection_pay_model/model_development/regression_multi_w_oot/outputs/
  761  aws s3 cp s3://collection-pay-model/model_development/outputs/multi_model_metrics.xlsx collection_pay_model/model_development/regression_multi_no_oot/outputs/
  762  cd src/
  763  jupyter notebook --ip=10.189.48.188
  764  cd src/
  765  jupyter notebook --ip=10.189.48.188
  766  cd src/
  767  jupyter notebook --ip=10.189.48.188
  768  cd src/
  769  jupyter notebook --ip=10.189.48.188
  770  cd src/
  771  aws s3 cp collection_pay_model/model_development/regression_multi_no_oot/ s3://collection-pay-model/model_development/
  772  ls collection_pay_model/model_development/regression_multi_no_oot/
  773  aws s3 sync collection_pay_model/model_development/regression_multi_no_oot/ s3://collection-pay-model/model_development/
  774  aws s3 sync collection_pay_model/model_development/regression_multi_no_oot/ s3://collection-pay-model/model_development
  775  aws-vault exec rhuang
  776  aws s3 sync collection_pay_model/model_development/regression_multi_no_oot/ s3://collection-pay-model/model_development
  777  aws s3 sync collection_pay_model/model_development/regression_multi_no_oot/ s3://collection-pay-model/model_development/
  778  cd src/
  779  aws-vault exec rhuang
  780  aws s3 cp collection_pay_model/model_development/regression_multi_no_oot/outputs/hgb_pred_scored_sample_vin201701.pkl s3://collection-pay-model/model_development/outputs/
  781  aws s3 cp collection_pay_model/model_development/regression_multi_no_oot/outputs/hgb_pred_scored_sample_vin201701.csv s3://collection-pay-model/model_development/outputs/
  782  aws s3 cp collection_pay_model/model_development/regression_multi_no_oot/outputs/hgb_pred_scored_sample_EOMDATE201801.csv s3://collection-pay-model/model_development/outputs/
  783  cd src/
  784  jupyter notebook --ip=10.189.48.188
  785  cd src/
  786  jupyter notebook --ip=10.189.48.188
  787  cd src/
  788  jupyter notebook --ip=10.189.48.188
  789  cd src/
  790  jupyter notebook --ip=10.189.48.188
  791  cd src/
  792  aws-vault exec rhuang
  793  jupyter notebook --ip=10.189.48.188
  794  aws s3 cp s3://cfm-dlq/GSCP_NN/D90_ECOT/d90_ecot_feat_imp.csv dq_models_cfmv3/GSCP_NN/D60_D90/
  795  aws s3 cp s3://cfm-dlq/GSCP_NN/D90_ECOT/d90_ecot_feat_imp.csv dq_models_cfmv3/GSCP_NN/D90_ECOT/
  796  aws s3 cp s3://cfm-dlq/GSCP_NN/D60_D90/d60_d90_feat_imp.csv dq_models_cfmv3/GSCP_NN/D60_D90/
  797  cd src/
  798  aws-vault exec rhuang
  799  exit
  800  cd src/
  801  jupyter notebook --ip=10.189.48.188
  802  exit
  803  cd src/
  804  aws-vault exec rhuang
  805  aws s3 cp s3://cfm-dlq-pipeline/PROD/P_missing_code.csv src/dq_models_pipeline_cfmv3/PROD/
  806  cd src/
  807  jupyter notebook --ip=10.189.48.188
  808  aws-vault exec rhuang
  809  aws s3 cp s3://collection-pay-model/model_development/ouputs/multi_model_metrics.xlsx src/collection_pay_model/model_development/regression_multi_no_oot_v2/outputs/
  810  aws s3 copy s3://collection-pay-model/model_development/ouputs/multi_model_metrics.xlsx src/collection_pay_model/model_development/regression_multi_no_oot_v2/outputs/
  811  aws s3 cp s3://collection-pay-model/model_development/outputs/multi_model_metrics.xlsx src/collection_pay_model/model_development/regression_multi_no_oot_v2/outputs/
  812  cd src/
  813  jupyter notebook --ip=10.189.48.188
  814  aws-vault exec rhuang
  815  cd src/
  816  jupyter notebook --ip=10.189.48.188
  817  cd src/
  818  jupyter notebook --ip=10.189.48.188
  819  cd src/
  820  jupyter notebook --ip=10.189.48.188
  821  cd src/
  822  jupyter notebook --ip=10.189.48.188
  823  cd src/
  824  jupyter notebook --ip=10.189.48.188
  825  cd src/
  826  jupyter notebook --ip=10.189.48.188
  827  cd src/
  828  jupyter notebook --ip=10.189.48.188
  829  exit
  830  cd src/
  831  jupyter notebook --ip=10.189.48.188
  832  aws ec2 stop-instances --instance-ids i-0113fa0134428fcdb
  833  cd src/
  834  jupyter notebook --ip=10.189.48.188
  835  cd src/
  836  jupyter notebook --ip=10.189.48.188
  837  cd src/
  838  ls 
  839  jupyter notebook --ip=10.189.48.188
  840  aws ec2 stop-instances --instance-ids i-0113fa0134428fcdb
  841  aws-vault exec rhuang
  842  cd src/
  843  aws s3 sync collection_pay_model/model_development/regression_multi_no_oot_v2/outputs/ s3://collection-pay-model/model_development/outputs
  844  aws-vault exec rhuang
  845  aws s3 sync collection_pay_model/model_development/regression_multi_no_oot_v2/outputs/ s3://collection-pay-model/model_development/outputs
  846  aws-vault exec rhuang
  847  cd src/
  848  jupyter notebook --ip=10.189.48.188
  849  aws-vault exec rhuang
  850  cd src/
  851  aws s3 sync collection_pay_model/model_development/regression_multi_no_oot_v2/outputs/missclassification_rates_by_ages/ s3://collection-pay-model/model_development/outputs
  852  aws s3 sync collection_pay_model/model_development/regression_multi_no_oot_v2/outputs/missclassification_rates_by_ages/ s3://collection-pay-model/model_development/outputs/missclassification_rates_by_ages/
  853  aws s3 sync collection_pay_model/model_development/regression_multi_no_oot_v2/outputs/missclassification_balances_by_ages/ s3://collection-pay-model/model_development/outputs/missclassification_balances_by_ages/
  854  df -h
  855  sudo mount -t cifs -o username=rhuang, uid=$(id -u),gid=$(id -g) //creditstrategyfiles.corp.na.greensky.net/CreditStrategy /mnt/CreditStrategy/
  856  cd ..
  857  sudo mount -t cifs -o username=rhuang, uid=$(id -u),gid=$(id -g) //creditstrategyfiles.corp.na.greensky.net/CreditStrategy /mnt/CreditStrategy/
  858  sudo mount -t cifs -o username=rhuang, uid=$(id -u),gid=$(id -g) //corpCorpShareFiles.corp.na.greensky.net/corp_share/Company Keep/Model Governance /mnt/Model Governance/
  859  aws s3 sync collection_pay_model/model_development/regression_multi_no_oot_v2/outputs/missclassification_balances_by_ages/ s3://collection-pay-model/model_development/outputs/missclassification_balances_by_ages/
  860  cd src/
  861  jupyter notebook --ip=10.189.48.188
  862  aws-vault exec rhuang
  863  cd src/
  864  jupyter notebook --ip=10.189.48.188
  865  sudo apt-get install tree
  866  sudo install tree
  867  yum install tree
  868  cd /src
  869  ls
  870  cd src/
  871  tree
  872  brew install tree
  873  yum install tree -y
  874  yum install tree 
  875  sudo yum install tree
  876  cd dq_models_cfmv3/
  877  tree
  878  tree -d
  879  cd ..
  880  cd dq_model_pipeline_cfmv3
  881  cd dq_models_pipeline_cfmv3/
  882  tree -d
  883  tree -L 1
  884  git status
  885  git push
  886  git status
  887  git add .
  888  git status
  889  git push
  890  git status
  891  git add Untitled.ipynb 
  892  git push
  893  cd src/
  894  cd dq_models_pipeline_cfmv3/
  895  conda activate cfm3_dq_pipeline
  896  conda activate --envs cfm3_dq_pipeline
  897  conda activate -- cfm3_dq_pipeline
  898  conda list
  899  conda envs
  900  conda env
  901  conda env list
  902  conda activate cfmv3_pipeline
  903  history
  904  bash ./back_book_exe.sh 202012
  905  cd src/
  906  jupyter notebook --ip=10.189.48.188
  907  cd src/
  908  jupyter notebook --ip=10.189.48.188
  909  cd src/
  910  jupyter notebook --ip=10.189.48.188
  911  cd src/
  912  jupyter notebook --ip=10.189.48.188
  913  cd  src/
  914  ls
  915  cd collection_pay_model/
  916  ls
  917  cd model_development/
  918  ls
  919  mv regression_l2_ageGt7 archives/
  920  ls
  921  cd archives/
  922  ls
  923  cd ..
  924  mv collection_pay_model_developement_HistGBM_ad_hoc_toDelete.ipynb collection_pay_model_developement_LGBM_Ensembles.ipynb collection_pay_model_developement_model_comparisions* archives/
  925  mv collection_pay_model_developement_regression_l2* archives/
  926  mv regression_l2_2 archives/
  927  mv regression_l2* archives/
  928  mv regression_multi_no_oot archives/
  929  mv regression_multi_w_oot* archives/
  930  mv lgbm_ensemble/ archives/
  931  mv auto_hyperparameter_tuning.ipynb auto_hp/
  932  mv model_0* archives/
  933  mv model_*.txt archives/
  934  mv HistGradientBoostingRegressor* archives/
  935  mv plot_poisson_regression_non_normal_loss.ipynb archives/
  936  mv gamma/ archives/
  937  mv regression_multi/ archives/
  938  cd
  939  cd src/
  940  git status
  941  cd collection_pay_model/
  942  git status
  943  git add >
  944  git add .
  945  git status
  946  ls 
  947  ls -al
  948  cat .gitignore
  949  git status
  950  git push
  951  git add *
  952  git add .
  953  git push
  954  git status
  955  git push
  956  git log
  957  git log -1
  958  git checkout master
  959  git status
  960  git stash
  961  git reset --hard
  962  git log -1
  963  git status
  964  git add .
  965  git checkout master
  966  git status
  967  git stash apply
  968  git status
  969  git add .
  970  git status
  971  git commit "folder updated with model devs files"
  972  git commit -m "folder updated with model devs files"
  973  git push
  974  git add .
  975  git commit -m "data and outputs folder added back"
  976  git push
  977  cd src/
  978  jupyter notebook --ip=10.189.48.188
  979  exi
  980  exit
  981  cd src/
  982  jupyter notebook --ip=10.189.48.188
  983  cd src/
  984  jupyter notebook --ip=10.189.48.188
  985  cd src/
  986  git status
  987  cd collection_pay_model/
  988  git status
  989  git add .
  990  git status
  991  git commit -m 'updated and organized codes'
  992  git push
  993  cd src/
  994  jupyter notebook --ip=10.189.48.188
  995  aws s3 sync collection_pay_model/ s3://collection-pay-model/
  996  aws s3 sync ./ s3://collection-pay-model/
  997  cd src/
  998  jupyter notebook --ip=10.189.48.188
  999  cd src/
 1000  jupyter notebook --ip=10.189.48.188
 1001  aws s3 sync dq_models_pipeline_cfmv3/ s3://cfm-dlq-pipeline/
