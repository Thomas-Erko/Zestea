fastqc_comp () {


    #mkdir qc_results

    #SRA-toolkit/FastQC/fastqc -o qc_results fastqer_$1/$1_1.fastq.gz fastqer_$1/$1_2.fastq.gz

    #unzip qc_results/$1_1_fastqc -d qc_results
    #unzip qc_results/$1_2_fastqc.zip -d qc_results

    sleep 2



}


fastqc_comp $1