node {
try{
stage ('Downloading git repository'){
    git branch: 'main', credentialsId: 'github', url: 'https://github.com/hemanth22/pythonapi_practise.git'
}
stage ('Build and execute'){
    sh 'python3 cowinhelper.py'
}
notify('Success')
}catch(err){
  notify("Error ${err}")
  currentBuild.result = 'FAILURE'
}
}

def notify(status){
    emailext (
      to: "hemanthbitra@live.com",
      subject: "${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
      body: """<p>${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
        <p>Check console output at <a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>""",
    )
}
