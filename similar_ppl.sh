#!/bin/bash

OUT_FILE=/output12
IN_FILE=/input/LargeDataset.txt
cd /home/hduser/
hadoop dfs -rm -R $OUT_FILE
hadoop jar ./hadoop-2.7.5/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar \
-D stream.map.output.field.separator=, \
-D stream.num.map.output.key.fields=2 \
-D map.output.key.field.separator=, \
-D num.key.fields.for.partition=1 \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options=-k1,2n \
-D mapred.map.tasks=20 \
-D mapred.reduce.tasks=24 \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input $IN_FILE \
-output $OUT_FILE \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
hadoop dfs -copyToLocal $OUT_FILE ./
