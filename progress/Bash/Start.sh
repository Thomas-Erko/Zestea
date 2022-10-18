## Automation ##

## Step 1 Creating the enviroment ##


## Step 2 File Preperation ##

fp () {
    # Make output directory 
    mkdir fastqer_$1
    SRA-toolkit/sratoolkit.3.0.0-mac64/bin/prefetch $1 --output-directory fastqer_$1
    sleep 5
}


fp $1
