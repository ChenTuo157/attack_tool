java -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -Xms512M -Xmx1024M -javaagent:Hook.jar -jar cobaltstrike.jar $*
