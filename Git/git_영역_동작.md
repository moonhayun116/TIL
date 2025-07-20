## Git 의 역할
1) 코드의 버전(히스토리)를 관리
   1) 개발되어 온 과정 파악
2) 이전 버전과의 변경 사항 비교

&rightarrow; 즉, git 은 코드의 **'변경 이력'** 을 기록하고 **'협업'** 을 원할하게 하는 도구이다.

## Git의 3가지 영역
1) **Working Directory**
   
   : 실제 작업 중인 파일들이 위치하는 영역
     
2) **Staging Area**
   
   : Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역이다.
   (다음 커밋에 포함될 변경 사항을 임시로 저장하는 공간)
 
3) **Repository(저장소)**
   
   : 버전(commit) 이력과 파일들이 영구적으로 저장되는 영역. 모든 버전(commmit)과 변경 이력이 기록됨
    * commit: 변경된 파일을 저장하는 행위이며, 마치 사진을 찍듯이 기록한다 하여 'snapshot'이라고도 한다.
  

## Git 의 동작

### `git init`
* 로컬 저장소 설정(초기화) &rightarrow; git의 버전 관리를 시작할 디렉토리에서 진행

* `git init` 명령어는 새로운 Git 저장소를 생성하거나, 기존 디렉토리를 Git 저장소로 초기화하는 데 사용된다. 이 명령어를 실행하면 현재 작업 디렉토리에 .git 디렉토리가 생성되며, 이 디렉토리는 해당 디렉토리에서 Git을 사용하여 버전 관리를 할 수 있도록 설정한다. 
  * 즉, git init은 프로젝트를 Git으로 관리하기 위한 첫 번째 단계라고 할 수 있다. 

1) 새로운 저장소 생성:
git init 명령어는 빈 디렉토리에서 새로운 Git 저장소를 만들 때 사용된다. 예를 들어, 새 프로젝트를 시작할 때 이 명령어를 사용하여 프로젝트 폴더를 Git으로 관리할 수 있도록 초기화한다. 

2) 기존 디렉토리 초기화:
이미 파일들이 있는 디렉토리에 git init을 실행하면, 해당 디렉토리가 Git 저장소로 변환된다. 이 경우에도 .git 디렉토리가 생성되며, 기존 파일들은 버전 관리를 위해 Git에 의해 추적된다. 

3) `.git` 디렉토리:
`git init`을 실행하면 현재 디렉토리에 .git이라는 숨김 폴더가 생성된다. 이 폴더는 Git 저장소의 핵심 데이터와 설정을 보관하는 곳이다. 

4) 버전 관리 시작:
`git init`을 실행한 후에는 다른 Git 명령어 (예: `git add`, `git commit`)를 사용하여 파일의 변경 사항을 기록하고, 버전 관리를 시작할 수 있다. 

* 사용 예시:
  * 새로운 저장소 생성:
  빈 폴더에서 `git init` 명령어를 실행 
  그러면 해당 폴더에 .git 디렉토리가 생성되고, Git 저장소로 초기화됨. 
  * 기존 디렉토리 초기화: 
  이미 파일들이 있는 폴더에서 `git init` 명령어를 실행 
  그러면 해당 폴더에 .git 디렉토리가 생성되고, 기존 파일들이 Git으로 관리됨. 

>### 🧠 참고
>
>`git init` 명령어는 로컬 저장소를 초기화하는 명령어다. 원격 저장소 (예: GitHub)와 연동하려면 추가적인 설정이 필요하다. 
>
>`git init`으로 생성된 .git 디렉토리는 삭제하지 않도록 주의해야 한다. ` .git` 디렉토리를 삭제하면 Git 저장소 정보가 사라져서 버전 관리가 불가능해진다. 
>
>또한 git 로컬 저장소 내에 또다른 git 로컬 저장소를 만들면 안된다. 즉, 이미 git 로컬 저장소인 디렉토리 내부 하단에서 `git init` 명령어를 다시 입력하면 안된다. (git 저장소 안에 git 저장소가 있을 경우 가장 바깥 쪽의 git  저장소가 안쪽의 git  저장소의 변경사항을 추적할 수 없기 때문)

### `git add`
변경사항이 있는 파일을 staging area에 추가

 * `git add <파일명>`: 특정 파일을 스테이징 영역에 추가한다. 예를 들어, `git add index.html`은 `index.html` 파일을 스테이징 영역에 추가한다다. 
   * `git add .` 또는 `git add *`: 현재 디렉토리와 하위 디렉토리의 모든 변경 사항을 스테이징 영역에 추가한다. 
   * `git add -p` 또는 `git add --patch`: 파일을 부분적으로 스테이징할 수 있다. 즉, 파일의 특정 부분만 선택하여 스테이징할 수 있다. 
  
### `git commit`

staging area에 있는 파일들을 저장소에 기록 &rightarrow; 해당 시점의 버전을 생성하고 변경 이력을 남기는 것


## Git 사용하기
1) 로컬 저장소 초기화
    * git의 관리를 받기 시작한 디렉토리 내에서는 (master)가 표시됨
    * `user@PC MINGW64 ~/DESKTOP/git_study/Git (master)`

2) `touch smalple.txt` 로 파일 생성 후 로컬 저장소의 파일 상태 확인(`git stauts`)
    ```bash
    No commits yet
    untracked files:
    (use "git add <file>..." to include in what will be committed)
            sample.txt
    ```
3) 파일을 staging area에 추가(`git add sample.txt`)
4) 로컬 저장소 파일 상태 확인
   ```bash
   On branch master

   No commits yet

   Changes to be committed:
    (use "git rm --cached <file>..." to un stage)
        new file: sample.txt
    ```
5) commit 생성
    * commit 작성자(author) 정보 설정 필요
    * `git config --global user.email "
    메일주소"`
    * `git config --global user.name "유저네임"`
6) commit 목록 확인(`git log`)
7) 로컬 저장소의 파일 상태 확인 (`git satus`)
    ```bash
    On branch master
    nothing to commit, working tree clean
    ```
8) `sample.txt`에 변경사항 만든 뒤 저장 &rightarrow; 로컬 저장소 파일 상태 확인
   ```bash
    modified: sample.txt 
    ```
9) 두 번째 commit 생성 후 확인



---
> ### 😎 참고
> * `git log --oneline` : commit 목록 한 줄로 보기
> * `git config --global -l`: git global 설정 정보 보기 
> * 파일명 잘못 만들었을 때: `git mv 원래파일명 고칠파일명`
>   * `fatal: not under version control`: 원래 파일 저장 안해서 생기는 오류이니 저장을 하고 하던지 아님 걍 mv 해줘도 된다~
> `rm -rf .git`: 깃 초기화 원상복귀
<img width="1831" height="686" alt="스크린샷 2025-07-20 162845" src="https://github.com/user-attachments/assets/cc6fdb67-59dc-4eb4-bdbc-a9ec95fa94b9" />
