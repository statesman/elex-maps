module.exports = function(grunt) {
  'use strict';

  // Project configuration.
  grunt.initConfig({

    // Transpile LESS
    less: {
      options: {
        paths: ['bower_components/bootstrap/less']
      },
      prod: {
        options: {
          compress: true,
          cleancss: true
        },
        files: {
          "dist/style.css": "src/css/style.less"
        }
      }
    },

    // Run our JavaScript through JSHint
    jshint: {
      js: {
        src: ['src/js/**.js']
      }
    },

    // Use Uglify to bundle up a pym file for the home page
    uglify: {
      options: {
        sourceMap: true
      },
      homepage: {
        files: {
          'dist/scripts.js': [
            'bower_components/jquery/dist/jquery.js',
            'bower_components/gmaps/gmaps.js',
            'bower_components/underscore/underscore.js',
            'bower_components/handlebars/handlebars.js',
            'bower_components/numeral/numeral.js',
            'src/js/palette.js',
            'src/js/key.js',
            'src/js/results.js',
            'src/js/main.js'
          ]
        }
      }
    }

  });

  // Load the task plugins
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-uglify');

  grunt.registerTask('default', ['jshint', 'uglify']);

};
