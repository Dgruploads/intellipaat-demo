pipeline {
	agent {label "build_server"}

	stages {
		stage ("This stage will build the package") {
			steps {
				sh "mvn clean"
				sh "mvn install"
			}
		}
	}
}
