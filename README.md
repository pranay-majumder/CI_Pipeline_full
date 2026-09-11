1. (mlops_venv) PS D:\MLOPS> cd Lecture_20_CI_2
2. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> dvc init
3. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git init
4. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git remote add origin <---->

> Intial folder we have created src (data,feature,model) and fastapi_app

5. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git add .
6. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git commit -m "Initial Commit"
7. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git push -u origin main

> Now Connect this Repo with Dagshub after Initial Commit to Github Repo

> Run Whole Pipeline for First Time
> It Create Experiment "CI Pipeline" in Mlflow
> It Create First Run "BOW_LOR_1" inside Experiment "CI Pipeline"
> It Store 1st Version of model (Version 1) into Model Registory with alias @champion
8. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> dvc repro


> Don't use pip freeze
> Just add necessary Library in requirements.txt, no need to specify version.
9. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> pip freeze > requirements.txt

10. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .dvc/.gitignore
        new file:   .dvc/config
        new file:   .dvcignore

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   params.yaml
        modified:   requirements.txt
        modified:   src/model/model_evaluation.py
        modified:   src/model/register_model.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .github/
        data/
        dvc.lock
        dvc.yaml
        errors.log
        feature_engineering_errors.log
        model_building_errors.log
        model_evaluation_errors.log
        model_registration_errors.log
        models/
        reports/
        transformation_errors.log


> Using Local Storage  
11. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2>  dvc remote add -d dvcremote_1 D:\MLOPS\DVC_Data_CI_Full
Setting 'dvcremote_1' as a default remote.

12. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> dvc remote list
dvcremote_1     D:\MLOPS\DVC_Data_CI_Full       (default)

13. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git add .
14. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git commit -m "Adding Second Experiment"
[main 3f731c7] Adding Second Experiment
 19 files changed, 282 insertions(+), 37 deletions(-)
 create mode 100644 .dvc/.gitignore
 create mode 100644 .dvc/config
 create mode 100644 .dvcignore
 create mode 100644 .github/workflows/ci.yaml
 create mode 100644 data/.gitignore
 create mode 100644 dvc.lock
 create mode 100644 dvc.yaml
 create mode 100644 errors.log
 create mode 100644 feature_engineering_errors.log
 create mode 100644 model_building_errors.log
 create mode 100644 model_evaluation_errors.log
 create mode 100644 model_registration_errors.log
 create mode 100644 models/.gitignore
 create mode 100644 reports/.gitignore
 create mode 100644 transformation_errors.log

> 
15. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> dvc push
Collecting                                                                   |13.0 [00:00,  136entry/s]
Pushing
13 files pushed

16. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git push -u origin main
Enumerating objects: 30, done.
Counting objects: 100% (30/30), done.
Delta compression using up to 12 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (23/23), 6.34 KiB | 590.00 KiB/s, done.
Total 23 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/pranay-majumder/CI_Pipeline_full.git
   68d9877..3f731c7  main -> main
branch 'main' set up to track 'origin/main'.

> commit (3f731c7) for that we use "dvc push".
> But here things are bit different so no need to use "dvc push"
> Just anlyze the Code on Experiment Tracking Purpose, not as Data Versioning Purpose.
> Here we change Parameter values inside "params.yaml" and initiate "git push", that will further trigger the CI Workflow and from CI Workflow it run "dvc repro"

17. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git log --oneline 
3f731c7 (HEAD -> main, origin/main) Adding Second Experiment
68d9877 Initial Commit

> In CI Pipeline also use same Python Version
18. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> python --version
Python 3.14.6


19. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .github/workflows/ci.yaml

> Here We Trigger CI Workflow Multiple Times, as we fail many times.

no changes added to commit (use "git add" and/or "git commit -a")
20. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git add .
21. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git commit -m "Adding Second Experiment again"
[main 25bddd6] Adding Second Experiment again
 1 file changed, 2 insertions(+), 2 deletions(-)
22. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git push -u origin main
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 415 bytes | 83.00 KiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/pranay-majumder/CI_Pipeline_full.git
   3f731c7..25bddd6  main -> main
branch 'main' set up to track 'origin/main'.


23. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git add .                                     
24. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git commit -m "Adding Second Experiment again"
[main c04c137] Adding Second Experiment again
 1 file changed, 2 insertions(+), 1 deletion(-)
25. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git push -u origin main                       
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 440 bytes | 110.00 KiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/pranay-majumder/CI_Pipeline_full.git
   25bddd6..c04c137  main -> main
branch 'main' set up to track 'origin/main'.


26. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git add .                                     
27. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git commit -m "Adding Second Experiment again"
[main dd287eb] Adding Second Experiment again
 2 files changed, 1 insertion(+), 2 deletions(-)
28. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git push -u origin main                       
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 628 bytes | 104.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/pranay-majumder/CI_Pipeline_full.git
   c04c137..dd287eb  main -> main
branch 'main' set up to track 'origin/main'.

26. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git add .                                     
27. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git commit -m "Adding Second Experiment again"
[main 6554953] Adding Second Experiment again
 1 file changed, 0 insertions(+), 0 deletions(-)
28. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git push -u origin main                       
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 323 bytes | 161.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/pranay-majumder/CI_Pipeline_full.git
   dd287eb..6554953  main -> main
branch 'main' set up to track 'origin/main'.
(mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git add .                                     
(mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git commit -m "Adding Second Experiment again"
[main 01578e5] Adding Second Experiment again
 1 file changed, 1 insertion(+), 1 deletion(-)
(mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git push -u origin main                       
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 407 bytes | 203.00 KiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/pranay-majumder/CI_Pipeline_full.git
   6554953..01578e5  main -> main
branch 'main' set up to track 'origin/main'.
(mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git add .                                     
(mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git commit -m "Adding Second Experiment again"
[main 4e348bd] Adding Second Experiment again
 1 file changed, 6 insertions(+), 2 deletions(-)
(mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git push -u origin main                       
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 12 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 577 bytes | 288.00 KiB/s, done.
Total 5 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To https://github.com/pranay-majumder/CI_Pipeline_full.git
   01578e5..4e348bd  main -> main
branch 'main' set up to track 'origin/main'.


29. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git add .                                     
30. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git commit -m "Adding Third Experiment"       
[main 11d0d85] Adding Third Experiment
 1 file changed, 2 insertions(+), 2 deletions(-)
31. (mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> git push -u origin main                
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 312 bytes | 312.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/pranay-majumder/CI_Pipeline_full.git
   4e348bd..11d0d85  main -> main
branch 'main' set up to track 'origin/main'.

(mlops_venv) PS D:\MLOPS\Lecture_20_CI_2> 

 > How to Generate Dagshub Token
 > Profile ---> Your Setting ---> Tokens ---> Generate New Token

 > How add this Token in Github Secrets
 > Open Repo ---> Setting ---> Secrets and Variables ---> Actions ---> New Repository Secrets

 > Here DVC Repro is running in CI Pipeline so we can't use "dvc push" here
















